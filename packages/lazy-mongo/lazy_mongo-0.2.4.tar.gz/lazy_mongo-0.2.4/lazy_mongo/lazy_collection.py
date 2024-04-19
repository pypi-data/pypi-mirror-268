from typing import Dict, NamedTuple
from pymongo.collection import Collection
from pymongo.errors import DuplicateKeyError
from .update_response import UpdateResponse
from .insert_response import InsertResponse


class LazyCollection(NamedTuple):
    collection: Collection

    def find_one(
        self,
        query: Dict = None,
        project: Dict = None,
    ):
        return self.collection.find_one(query, project)

    def find(
        self,
        query: Dict = None,  # type: ignore
        project: Dict = None,  # type: ignore
    ):
        return self.collection.find(query, project)

    def insert_one(
        self,
        document: Dict = None,  # type: ignore
    ):
        try:
            result = self.collection.insert_one(document)

            return InsertResponse(
                ok=True,
                result=result,
            )

        except DuplicateKeyError as e:
            return InsertResponse(
                ok=False,
                is_duplicate=True,
                error=e,
            )

        except Exception as e:
            return InsertResponse(
                ok=False,
                error=e,
            )

    def update_set_one(
        self,
        filter: Dict = None,  # type: ignore
        document: Dict = None,  # type: ignore
    ):
        try:
            result = self.collection.update_one(
                filter=filter,
                update={
                    "$set": document,
                },
                upsert=False,
            )

            return UpdateResponse(
                ok=True,
                result=result,
            )

        except DuplicateKeyError as e:
            return UpdateResponse(
                ok=False,
                is_duplicate=True,
                error=e,
            )

        except Exception as e:
            return UpdateResponse(
                ok=False,
                error=e,
            )

    def count(
        self,
        query: Dict = None,  # type: ignore
    ):
        return self.collection.count_documents(query)

    def distinct(self, key: str):  # type: ignore
        return self.collection.distinct(key)
