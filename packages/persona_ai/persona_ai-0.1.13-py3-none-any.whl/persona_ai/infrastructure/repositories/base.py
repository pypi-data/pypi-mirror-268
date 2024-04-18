from abc import ABC, abstractmethod


class Repository(ABC):
    """
    This class is the base interface for all repositories.
    """

    @abstractmethod
    def find(
        self,
        filter: dict = None,
        sort: dict = None,
        limit: int = None,
        skip: int = None,
    ):
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id):
        raise NotImplementedError

    @abstractmethod
    def create(self, entity):
        raise NotImplementedError

    @abstractmethod
    def delete(self, id: str):
        raise NotImplementedError

    @abstractmethod
    def update(self, entity):
        raise NotImplementedError

    def count(self, query: dict = None) -> int:
        raise NotImplementedError
