from typing import Generic, Iterable, Optional, TypeVar
from abc import ABC

T = TypeVar("T")


class IRepository(ABC):
    @classmethod
    def save(self, item: T) -> T:
        pass

    @classmethod
    def delete(self, item: T) -> None:
        pass

    @classmethod
    def deleteById(self, id: int) -> None:
        pass

    @classmethod
    def findAll(self) -> Iterable[T]:
        pass

    @classmethod
    def findById(self, id: int) -> Optional[T]:
        pass

    @classmethod
    def existsById(self, id: int) -> bool:
        pass

    @classmethod
    def count(self) -> int:
        pass
