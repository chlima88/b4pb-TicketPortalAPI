from typing import Iterable, Optional
from models.user import User, UserDTO
from abc import ABC


class IRepository(ABC):
    @classmethod
    def save(self, user: User) -> User:
        pass

    @classmethod
    def delete(self, user: User) -> None:
        pass

    @classmethod
    def deleteById(self, id: int) -> None:
        pass

    @classmethod
    def findAll(self) -> Iterable[User]:
        pass

    @classmethod
    def findById(self, id: int) -> Optional[User]:
        pass

    @classmethod
    def existsById(self, id: int) -> bool:
        pass

    @classmethod
    def count(self) -> int:
        pass
