from typing import Iterable
from fastapi import APIRouter

from models.ticket import Ticket, TicketDTO
from services.service import Service
from repositories.repository import Repository
from dataloaders.dataloader import DataLoader


ticketController = APIRouter(prefix="/tickets")
ticketRepository = Repository()
ticketService = Service[Ticket](ticketRepository)
DataLoader.load(Ticket, ticketRepository, "./dataloaders/data/Tickets.csv")


@ticketController.post("/", status_code=201)
async def post(ticketDTO: TicketDTO) -> TicketDTO:
    return ticketService.create(ticketDTO)


@ticketController.get("/{id}", status_code=200, response_model=TicketDTO)
async def get(id: int) -> TicketDTO:
    return ticketService.getById(id)


@ticketController.get("/", status_code=200)
async def getAll() -> Iterable[TicketDTO]:
    return ticketService.getAll()


@ticketController.delete("/{id}", status_code=204)
async def delete(id: int) -> None:
    ticketService.remove(id)
