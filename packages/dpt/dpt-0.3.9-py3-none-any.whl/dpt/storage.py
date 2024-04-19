from __future__ import annotations
from pymongo import MongoClient
from pymongo.database import Database as MongoDatabase
from pymongo.collection import Collection
from typing import Any
import jsonschema
import copy


class ConnectionInfo:
    def __init__(self, connectionString):
        self.connectionString = connectionString
        # if self.connectionString == None:
        #     from .system import system
        #     self.connectionString = system.db_connection_string
        self._instance = None

    def instance(self) -> MongoClient:
        if self._instance == None:
            self._instance = MongoClient(self.connectionString)
        return self._instance


class DatabaseInfo:
    def __init__(
        self,
        name: str = None,
        connection: ConnectionInfo = None,
        instance: MongoDatabase = None,
    ):
        if instance != None:
            self._instance = instance
        else:
            self.name = name
            self.connection = connection
            self._instance = None

    def instance(self) -> MongoDatabase:
        if self._instance == None:
            self._instance = self.connection.instance()[self.name]
        return self._instance


class CollectionInfo:
    def __init__(self, collectionName: str, database: DatabaseInfo):
        self._collection_name = collectionName
        self.name = collectionName
        self.database = database
        self._count = 0
        # if self.database == None:
        #     self.database = Database()
        self._instance = None

    def get_count(self):
        return self._count

    def get_info(self):
        return f"collection '{self.name}'"

    def instance(self) -> Collection:
        if self._instance == None:
            self._instance = self.database.instance()[self.name]
        return self._instance

    def _update_count_from_collection(self):
        self._count = self.instance().count_documents({})


class DbReader(CollectionInfo):
    def __init__(self, collectionName: str, database: DatabaseInfo = None):
        super().__init__(collectionName, database)

    def read_all(self):
        self._count = self.instance().count_documents({})
        print(f"read {self._count} documents from {self.get_info()}")

        return self.instance().find({})

    def read_one(self):
        self._count += 1
        return self.instance().find_one({})

    def _prepare_pipeline(self, pipeline: list[dict]):
        orig_pipeline = pipeline
        pipeline: list[dict] = []
        for step in orig_pipeline:
            pipeline.append(step.copy())

        def bad_ref_text(step, coll_ref):
            return f'Incorrect collection reference `{coll_ref}`. Use reader object to reference collection, e. g. "from": task.get_named_reader("coll_to_join"). Incorrect step: \n {step}'

        def first_of(d) -> tuple[str, dict]:
            for key, value in d.items():
                return key, value

        for step in pipeline:
            step_name, step = first_of(step)
            if step_name in ["$lookup", "$graphLookup", "$unionWith"]:
                coll_ref = step.get("from") or step.get("coll")
                if isinstance(coll_ref, DbReader):
                    step["from"] = coll_ref._collection_name
                else:
                    raise Exception(bad_ref_text(step, coll_ref))

    def aggregate(self, out: DbWriter, pipeline: list[dict[str, Any]]):
        self._update_count_from_collection()
        self._prepare_pipeline(pipeline)
        pipeline.append({"$out": out._collection_name})
        print(f"read {self._count} documents from {self.get_info()}")
        print("run aggregation:\n", pipeline)
        self.instance().aggregate(pipeline)
        out._update_count_from_collection()
        out.close()


class MemoryReader:
    def __init__(self, data: list[dict[str, Any]], schema: dict):
        self._data = data
        self.schema = schema

    def _validate(self):
        if self.schema == None:
            return
        for item in self._data:
            jsonschema.validate(instance=item, schema=self.schema)

    def get_count(self):
        return len(self._data)

    def get_info(self):
        return f"list[]"

    def read_all(self):
        self._validate()
        print(f"read {len(self._data)} documents from {self.get_info()}")
        return self._data

    def read_one(self) -> Any | None:
        self._validate()
        if len(self._data) == 0:
            return None
        return self._data[0]


class DbWriter(CollectionInfo):
    def __init__(self, collectionName: str, database: DatabaseInfo = None):

        super().__init__(collectionName, database)
        self._closed = True

    def clear(self):
        self.instance().delete_many({})

    def write_many(self, documents: list[dict]):
        if len(documents) > 0:
            self.instance().insert_many(documents)
        self._count += len(documents)
        self._closed = False

    def close(self):
        self._closed = True
        print(f"loaded {self._count} documents into {self.get_info()}")

    def is_closed(self):
        return self._closed


class MemoryWriter:
    def __init__(self, data: list[dict[str, Any]]):
        self._data = data
        self._count = 0
        self._closed = True

    def get_info(self):
        return f"list[]"

    def clear(self):
        self._data.clear()

    def write_many(self, documents: list[dict]):
        self._data.extend(documents)
        self._count += len(documents)
        self._closed = False

    def close(self):
        print(f"loaded {self._count} documents into {self.get_info()}")
        self._closed = True

    def is_closed(self):
        return self._closed
