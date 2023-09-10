from typing import Iterable, TypeVar
from interfaces.repository_interface import IRepository

T = TypeVar("T")


class Service:
    def __init__(self, repository: IRepository):
        self.repository = repository

    def create(self, ticketDTO: T) -> T:
        id = self.repository.count()
        ticketDTO.id = id
        ticket = T(**ticketDTO.model_dump())
        return self.repository.save(ticket)

    def getAll(self) -> Iterable[T]:
        return self.repository.findAll()

    def getById(self, id: int) -> T:
        ticket = self.repository.findById(id)
        return ticket

    def remove(self, id: int) -> None:
        self.repository.deleteById(id)
