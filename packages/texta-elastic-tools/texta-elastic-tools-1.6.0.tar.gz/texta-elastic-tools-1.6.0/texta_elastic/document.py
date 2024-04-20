import datetime
import json
import logging
import uuid
from typing import List, Optional

import elasticsearch
import elasticsearch_dsl
from elasticsearch.helpers import bulk
from elasticsearch_dsl import Q, Search

from texta_elastic.core import ElasticCore
from texta_elastic.decorators import elastic_connection
from texta_elastic.searcher import EMPTY_QUERY
from texta_elastic.settings import ERROR_LOGGER, TEXTA_ANNOTATOR_KEY, TEXTA_TAGS_KEY


class ESDocObject:
    """
    An object connected to ES document. Retrieves the document from ES on init.
    """

    def __init__(self, document_id=None, index: str = None, document=None, elastic_core: Optional[ElasticCore] = None):
        self.core = elastic_core or self._get_core()
        self.document_id = document_id
        self.index = index
        self.document = self.get() if document_id else document

    def _get_core(self):
        return ElasticCore()

    @elastic_connection
    def get(self):
        """
        Retrieve document by ID.
        """
        document = self.core.es.get(self.index, self.document_id)
        return {
            "_index": document["_index"],
            "_type": document["_type"],
            "_id": document["_id"],
            "_source": document["_source"]
        }

    @staticmethod
    @elastic_connection
    def random_document(indices, query=EMPTY_QUERY, elastic_core: Optional[ElasticCore] = None):
        ec = elastic_core or ElasticCore()
        s = elasticsearch_dsl.Search(using=ec.es, index=indices)
        query = query.get("query", None) or query
        existing_query = Q(query)  # TODO Depending on whether you pull annotated or normal this becomes messy, fix later.
        random_query = Q("function_score", random_score={})
        s = s.query("bool", must=[existing_query, random_query])
        s = s.source(exclude=["*"])
        s = s.extra(size=1)
        hits = s.execute()
        for hit in hits:
            return ESDocObject(document_id=hit.meta.id, index=hit.meta.index)
        return None

    def apply_mlp(self, mlp, analyzers: List[str], field_data: List[str]):
        """
        Applies MLP to the selected fields and combines the results.
        """
        document_source = self.document["_source"]
        mlp_processed = mlp.process_docs([document_source], analyzers=analyzers, doc_paths=field_data)[0]
        self.document["_source"] = {**document_source, **mlp_processed}
        return True

    def add_field(self, field_name: str, field_content):
        """
        Adds field to document source.
        """
        self.document["_source"][field_name] = field_content
        return True

    @staticmethod
    def generate_fact_template(source="annotator"):
        """
        Pre-generates some fields to be added as a fact in the context of the annotator.
        :return:
        """
        return {"id": str(uuid.uuid4()), "source": source}

    def add_fact(self, fact_name, fact_value, doc_path, spans=json.dumps([[0, 0]]), sent_index=0, author="", source="annotator"):
        template_fact = self.generate_fact_template(source=source)
        fact = {**template_fact, "str_val": fact_value, "fact": fact_name, "doc_path": doc_path, "spans": spans, "sent_index": sent_index, "author": author}
        existing_facts = self.document["_source"].get(TEXTA_TAGS_KEY, [])
        existing_facts.append(fact)
        existing_facts = ElasticDocument.remove_duplicate_facts(existing_facts)
        self.document["_source"][TEXTA_TAGS_KEY] = existing_facts
        return fact

    def filter_facts(self, fact_name, doc_path):
        new_facts = []
        existing_facts = self.document["_source"].get(TEXTA_TAGS_KEY, [])

        for fact in existing_facts:
            if fact["fact"] != fact_name or fact["doc_path"] != doc_path:
                new_facts.append(fact)

        self.document["_source"][TEXTA_TAGS_KEY] = new_facts

        return new_facts

    # TODO These three can be unified into a more general function.
    def add_skipped(self, annotator_model, user):
        job_dict = {
            "job_id": annotator_model.pk,
            "user": user.username,
            "skipped_timestamp_utc": datetime.datetime.utcnow()
        }
        self.document["_source"][TEXTA_ANNOTATOR_KEY] = job_dict


    def add_annotated(self, annotator_model, user):
        job_dict = {
            "job_id": annotator_model.pk,
            "user": user.username,
            "processed_timestamp_utc": datetime.datetime.utcnow()
        }
        self.document["_source"][TEXTA_ANNOTATOR_KEY] = job_dict

    @elastic_connection
    def update(self, retry_on_conflict=3, refresh="wait_for"):
        """
        Updates document in ES by ID.
        """
        return self.core.es.update(
            index=self.document["_index"],
            doc_type=self.document["_type"],
            id=self.document["_id"] or self.document_id,
            body={"doc": self.document["_source"]},
            refresh=refresh,
            retry_on_conflict=retry_on_conflict
        )

    @elastic_connection
    def delete(self, ignore=()):
        """
        Removes given document from ES.
        """
        return self.core.es.delete(index=self.index, id=self.document_id, ignore=ignore)


class ElasticDocument:
    """
    Everything related to managing documents in Elasticsearch
    """

    def __init__(self, index, elastic_core: Optional[ElasticCore] = None):
        self.index = index
        self.core = elastic_core or self._get_core()

    def _get_core(self):
        return ElasticCore()

    @staticmethod
    def remove_duplicate_facts(facts: List[dict]):
        if facts:
            set_of_jsons = {json.dumps(fact, sort_keys=True, ensure_ascii=False) for fact in facts}
            without_duplicates = [json.loads(unique_fact) for unique_fact in set_of_jsons]
            return without_duplicates
        else:
            return []

    def __does_fact_exist(self, fact: dict, existing_facts: List[dict]):
        existing = {json.dumps(d, sort_keys=True, ensure_ascii=True) for d in existing_facts}
        checking = json.dumps(fact, sort_keys=True, ensure_ascii=True)
        if checking in existing:
            return True
        else:
            return False

    def _fact_addition_generator(self, documents, fact, retry_on_conflict=3):
        checked_indices = set()
        for document in documents:
            index_name = document["_index"]
            # If there is no texta_facts field in the index, add it.
            if index_name not in checked_indices and TEXTA_TAGS_KEY not in document["_source"]:
                self.core.add_texta_facts_mapping(index_name)
                checked_indices.add(index_name)

            if not self.__does_fact_exist(fact, document["_source"][TEXTA_TAGS_KEY]):
                facts = document["_source"][TEXTA_TAGS_KEY]
                facts.append(fact)
                doc_type = document.get("_type", "_doc")
                yield {
                    "_op_type": "update",
                    "retry_on_conflict": retry_on_conflict,
                    "_index": index_name,
                    "_type": doc_type,
                    "_id": document["_id"],
                    "doc": {TEXTA_TAGS_KEY: facts}
                }

    @elastic_connection
    def add_fact_to_documents(self, fact: dict, doc_ids: List):
        # Fetch the documents with the bulk function to get the facts,
        # and to validate that those ids also exist.
        documents = self.get_bulk(doc_ids=doc_ids, fields=[TEXTA_TAGS_KEY])
        generator = self._fact_addition_generator(documents, fact)
        self.bulk_update(generator)
        return True

    @elastic_connection
    def get(self, doc_id, fields: List = None):
        """
        Retrieve document by ID.
        """
        s = Search(using=self.core.es, index=self.index)
        s = s.query("ids", values=[doc_id])
        s = s.source(fields)
        s = s[:1000]
        response = s.execute()
        if response:
            document = response[0]
            doc_type = getattr(document.meta, "doc_type", "_doc")
            return {"_index": document.meta.index, "_type": doc_type, "_id": document.meta.id, "_source": document.to_dict()}
        else:
            return None

    @elastic_connection
    def get_bulk(self, doc_ids: List[str], fields: List[str] = None, flatten: bool = False) -> List[dict]:
        """
        Retrieve full Elasticsearch documents by their ids that includes id, index,
        type and content information. For efficiency, it's recommended to limit the returned
        fields as unneeded content consumes extra internet bandwidth.
        """
        s = Search(using=self.core.es, index=self.index)
        s = s.query("ids", values=doc_ids)
        s = s.source(fields)
        s = s[:10000]
        response = s.execute()
        if response:
            container = []
            for document in response:
                document = {
                    "_index": document.meta.index,
                    "_type": getattr(document.meta, "doc_type", "_doc"),
                    "_id": document.meta.id,
                    "_source": self.core.flatten(document.to_dict()) if flatten else document.to_dict()
                }
                container.append(document)
            return container
        else:
            return []

    @elastic_connection
    def update(self, index, doc_id, doc, doc_type="_doc", retry_on_conflict=3, refresh="wait_for"):
        """
        Updates document in ES by ID.
        """
        return self.core.es.update(index=index, doc_type=doc_type, id=doc_id, body={"doc": doc}, refresh=refresh, retry_on_conflict=retry_on_conflict)

    def normalise_update_actions(self, generator, retry_on_conflict: int = 3):
        """
        Ensures that all the actions sent into the bulk_update wrapper will be in the proper
        format with all the required parameters that are unique to updating.
        """
        for action in generator:
            action["_op_type"] = "update"
            action["retry_on_conflict"] = retry_on_conflict

            # In cases the user puts in _source by accident instead of doc.
            if "_source" in action:
                source = action.pop("_source")
                action["doc"] = source

            yield action

    def bulk_update(self, actions, refresh="wait_for", chunk_size: int = 100, request_timeout: int = 30, retry_on_conflict: int = 3):
        """
        Intermediary function to commit bulk updates.
        This function doesn't have actions processing because it's easier to use
        when it's index unaware. Actions should be processed when needed.

        Since this function changes _source fields into doc (as needed by update operations), passing
        raw Elasticsearch documents is fitting.

        Setting refresh to "wait_for" makes Python wait until the documents are actually indexed
        to avoid version conflicts.

        Args:
            chunk_size: How many documents should be sent per batch.
            refresh: Which behaviour to use for updating the index contents on a shard level.
            actions: List of dictionaries or its generator containing raw Elasticsearch documents, for ex:
            {"_id": 1234, "_index": "reddit", "op_type": "update", "doc": {"texta_facts": []}}
            request_timeout: How many seconds until a timeout exception is launched.
            retry_on_conflict: How many times to retry on an Elasticsearch conflict exception.

        Returns: Elasticsearch response to the request.
        """
        actions = self.add_type_to_docs(actions)
        actions = self.normalise_update_actions(actions, retry_on_conflict=retry_on_conflict)
        return bulk(client=self.core.es, actions=actions, refresh=refresh, request_timeout=request_timeout, chunk_size=chunk_size)

    @elastic_connection
    def add(self, doc, refresh="wait_for"):
        """
        Adds document to ES.
        """
        return self.core.es.index(index=self.index, body=doc, refresh=refresh)

    @elastic_connection
    def bulk_add(self, docs, chunk_size=100, raise_on_error=True, stats_only=True):
        actions = [{"_index": self.index, "_source": doc, "_type": doc.get("_type", "_doc")} for doc in docs]
        return bulk(client=self.core.es, actions=actions, chunk_size=chunk_size, stats_only=stats_only, raise_on_error=raise_on_error)

    def add_type_to_docs(self, actions):
        for action in actions:
            doc_type = action.get("_type", "_doc")
            action["_type"] = doc_type
            yield action

    @elastic_connection
    def bulk_add_generator(self, actions, chunk_size=100, raise_on_error=True, stats_only=True, refresh="wait_for"):
        actions = self.add_type_to_docs(actions)
        try:
            return bulk(client=self.core.es, actions=actions, chunk_size=chunk_size, stats_only=stats_only, raise_on_error=raise_on_error, refresh=refresh)
        except elasticsearch.helpers.errors.BulkIndexError as e:
            logging.getLogger(ERROR_LOGGER).exception(e.args[1][0]['index']['error']['reason'], exc_info=False)
            return None

    @elastic_connection
    def delete(self, doc_id: str, ignore=()):
        """
        Removes given document from ES.
        """
        return self.core.es.delete(index=self.index, id=doc_id, ignore=ignore)

    @elastic_connection
    def delete_by_query(self, query: dict):
        """
        Removes given document from ES.
        """
        return self.core.es.delete_by_query(index=self.index, body=query)

    @elastic_connection
    def bulk_delete(self, document_ids: List[str], wait_for_completion=True):
        query = Search().query(Q("ids", values=document_ids)).to_dict()
        response = self.core.es.delete_by_query(index=self.index, body=query, wait_for_completion=wait_for_completion)
        return response

    @elastic_connection
    def count(self, indices=None) -> int:
        """
        Returns the document count for given indices.
        :indices: Either a coma separated string of indices or a list of index strings.
        """
        index = indices if indices else self.index
        return self.core.es.count(index=index)["count"]
