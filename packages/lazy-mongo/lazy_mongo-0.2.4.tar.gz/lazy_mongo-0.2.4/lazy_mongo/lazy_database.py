from typing import Dict, NamedTuple
from pymongo.database import Database
from .lazy_collection import LazyCollection


class LazyDatabase(NamedTuple):
    database: Database
    default_collection_name: str = None  # type: ignore

    def __getitem__(self, key: str):
        return LazyCollection(self.database[key])

    def find_one(
        self,
        collection: str = None,
        query: Dict = None,
        project: Dict = None,
    ):
        coll = self[collection or self.default_collection_name]

        return coll.find_one(query, project)

    def find(
        self,
        collection: str = None,  # type: ignore
        query: Dict = None,  # type: ignore
        project: Dict = None,  # type: ignore
    ):
        coll = self[collection or self.default_collection_name]

        return coll.find(query, project)

    def insert_one(
        self,
        collection: str = None,  # type: ignore
        document: Dict = None,  # type: ignore
    ):
        coll = self[collection or self.default_collection_name]

        return coll.insert_one(document)

    def update_set_one(
        self,
        collection: str = None,  # type: ignore
        filter: Dict = None,  # type: ignore
        document: Dict = None,  # type: ignore
    ):
        coll = self[collection or self.default_collection_name]

        return coll.update_set_one(filter, document)

    def count(
        self,
        collection: str = None,  # type: ignore
        query: Dict = None,  # type: ignore
    ):
        coll = self[collection or self.default_collection_name]

        return coll.count(query)

    def distinct(
        self,
        key: str,
        collection: str = None,  # type: ignore
    ):
        coll = self[collection or self.default_collection_name]

        return coll.distinct(key)
