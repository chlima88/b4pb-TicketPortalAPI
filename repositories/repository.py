from typing import Iterable, TypeVar

from interfaces.repository_interface import IRepository

T = TypeVar("T")


class Repository(IRepository):
    def __init__(self, idSeed: int = 1):
        self.__db: Iterable[T] = []
        self.__lastId = idSeed

    @property
    def lastId(self):
        return self.__lastId

    def save(self, item: T) -> T:
        user = {**item.model_dump()}
        user["id"] = self.__lastId
        self.__db.append(user)
        self.__lastId += 1
        return user

    def delete(self, item: T) -> None:
        raise NotImplementedError

    def deleteById(self, id: int) -> None:
        item = self.findById(id)
        self.__db.pop(self.__db.index(item))

    def findAll(self) -> Iterable[T]:
        return self.__db

    def findById(self, id: int) -> T:
        for item in self.__db:
            if item["id"] == id:
                return item
        raise Exception("ID not found")

    def existsById(self, id: int) -> bool:
        for item in self.__db:
            if item.id == id:
                return True
            return False

    def count(self) -> int:
        return len(self.__db)
