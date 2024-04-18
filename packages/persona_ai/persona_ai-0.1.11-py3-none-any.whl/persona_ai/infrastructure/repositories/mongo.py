from os import getenv
from typing import Generic, TypeVar, List, Type

from pydantic import BaseModel
from pymongo import MongoClient

from persona_ai.infrastructure.repositories.base import Repository


class MongoHelper:
    """
    Helper class to manage the MongoDB connection.
    """

    mongo_client: MongoClient | None

    def __init__(self):
        self.mongo_client = None

    def get_client(self) -> MongoClient:
        if self.mongo_client is None:
            self.mongo_client = create_mongo_client()

        return self.mongo_client

    def get_database(self):
        return self.get_client().get_database()

    def get_collection(self, collection_name):
        return self.get_database().get_collection(collection_name)


mongo_helper = MongoHelper()


def create_mongo_client() -> MongoClient:
    url = getenv("MONGO_URL")
    if url is None:
        raise Exception("Please set MONGO_URL environment variable")

    return MongoClient(url)


TEntity = TypeVar("TEntity", bound=BaseModel)


def _rename__id_to_id(entity: dict) -> dict:
    entity["id"] = entity.pop("_id")
    return entity


def _rename_id_to__id(entity: dict) -> dict:
    entity["_id"] = entity.pop("id")
    return entity


class MongoRepository(Repository, Generic[TEntity]):
    """
    A generic repository implementation for MongoDB.
    """

    collection_name: str
    model_type: Type[TEntity]

    def __init__(self, collection_name: str, model_type: Type[TEntity]):
        self.collection = mongo_helper.get_collection(collection_name)
        self.model_type = model_type

    def map_to_model(self, entity: dict) -> TEntity:
        return self.model_type(**entity) if entity is not None else None

    def find(
        self,
        filter: dict = None,
        sort: dict = None,
        limit: int = 0,
        skip: int = 0,
    ) -> List[TEntity]:
        entities = self.collection.find(
            filter=filter, sort=sort, limit=limit, skip=skip
        )
        return [self.map_to_model(_rename__id_to_id(entity)) for entity in entities]

    def get_by_id(self, id) -> TEntity:
        entity = self.collection.find_one({"_id": id})
        return (
            self.map_to_model(_rename__id_to_id(dict(entity)))
            if entity is not None
            else None
        )

    def exists(self, id) -> bool:
        return self.collection.count_documents({"_id": id}) > 0

    def create(self, entity: TEntity):
        return self.collection.insert_one(
            _rename_id_to__id(entity.model_dump(by_alias=True))
        )

    def delete(self, id):
        return self.collection.delete_one({"_id": id})

    def update(self, entity: TEntity):
        dump = entity.model_dump(by_alias=True)
        # rename id property to _id
        dump["_id"] = dump.pop("id")
        return self.collection.update_one({"_id": dump["_id"]}, {"$set": dump})
