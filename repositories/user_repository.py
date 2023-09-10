from typing import Iterable
from models.user import User
from interfaces.repository_interface import IRepository


class UserRepository(IRepository):
    __state = {}
    __db: Iterable[User] = []

    def __init__(self):
        self.__dict__ = self.__state

    def save(self, user: User) -> User:
        self.__db.append(user)
        return user

    def delete(self, user: User) -> None:
        raise NotImplementedError

    def deleteById(self, id: int) -> None:
        user = self.findById(id)
        self.__db.pop(self.__db.index(user))

    def findAll(self) -> Iterable[User]:
        return self.__db

    def findById(self, id: int) -> User:
        for user in self.__db:
            if user.id == id:
                return user

        raise Exception("ID não encontrado")

    def existsById(self, id: int) -> bool:
        for user in self.__db:
            if user.id == id:
                return True
            return False

    def count(self) -> int:
        return len(self.__db)
