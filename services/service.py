from typing import Generic, Iterable, TypeVar
from interfaces.repository_interface import IRepository

T = TypeVar("T")


class Service(Generic[T]):
    def __init__(self, repository: IRepository):
        self.repository = repository

    def create(self, dto: T) -> T:
        return self.repository.save(dto)

    def getAll(self) -> Iterable[T]:
        return self.repository.findAll()

    def getById(self, id: int) -> T:
        ticket = self.repository.findById(id)
        return ticket

    def remove(self, id: int) -> None:
        self.repository.deleteById(id)
