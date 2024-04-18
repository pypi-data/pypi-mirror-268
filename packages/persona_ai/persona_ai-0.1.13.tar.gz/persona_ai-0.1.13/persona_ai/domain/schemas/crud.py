from typing import List, Any

from pydantic import BaseModel

FILTER_TYPES = [
    "like",
    "gt",
    "ne",
    "gte",
    "lt",
    "lte",
    "eq",
    "in",
    "nin",
    "or",
    "and",
    "custom",
    "range",
    "exists",
    "is",
]


class Sort(BaseModel):
    property: str
    descending: bool


class Filter(BaseModel):
    property: str
    value: Any
    type: str


class Projection(BaseModel):
    property: str
    visible: bool


class CrudQuery(BaseModel):
    page: int
    rowsPerPage: int
    sorts: List[Sort]
    filters: List[Filter]
    projections: List[Projection]
