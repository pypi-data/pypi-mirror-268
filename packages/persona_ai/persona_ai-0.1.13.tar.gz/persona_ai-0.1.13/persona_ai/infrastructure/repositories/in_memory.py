import operator
from typing import Generic, TypeVar, List, Type

from pydantic import BaseModel

from persona_ai.infrastructure.repositories.base import Repository

TEntity = TypeVar("TEntity", bound=BaseModel)


def _get_nested_value(obj, key):
    keys = key.split(".")
    for k in keys:
        if isinstance(obj, dict):
            obj = obj.get(k)
        else:
            obj = getattr(obj, k, None)
    return obj


class InMemoryRepository(Repository, Generic[TEntity]):
    """
    A generic repository implementation for in-memory storage.
    """

    model_type: Type[TEntity]
    data: dict

    def __init__(self, model_type: Type[TEntity]):
        self.model_type = model_type
        self.data = {}

    def map_to_model(self, entity: dict) -> TEntity:
        return self.model_type(**entity) if entity is not None else None

    def find(
        self,
        filter: dict = None,
        sort: dict = None,
        limit: int = 0,
        skip: int = 0,
    ) -> List[TEntity]:
        entities = list(self.data.values())

        # Apply filter
        if filter:
            filtered_entities = [
                entity
                for entity in entities
                if all(
                    operator.eq(_get_nested_value(entity, k), v)
                    for k, v in filter.items()
                )
            ]
            entities = filtered_entities

        # Apply sort
        if sort:
            for sort_key, sort_order in reversed(sort.items()):
                entities = sorted(
                    entities, key=operator.itemgetter(sort_key), reverse=sort_order < 0
                )

        # Apply skip and limit
        entities = entities[skip : (skip + limit if limit != 0 else len(entities))]

        return [self.map_to_model(entity) for entity in entities]

    def get_by_id(self, id) -> TEntity:
        entity = self.data.get(id)
        return self.map_to_model(entity) if entity is not None else None

    def exists(self, id) -> bool:
        return id in self.data

    def create(self, entity: TEntity):
        self.data[entity.id] = entity.model_dump()

    def delete(self, id):
        if id in self.data:
            del self.data[id]

    def update(self, entity: TEntity):
        self.data[entity.id] = entity.model_dump()
