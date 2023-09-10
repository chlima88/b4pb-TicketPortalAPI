from typing import Iterable
from fastapi import APIRouter, HTTPException

from models.ticket import Ticket, TicketDTO
from services.service import Service
from repositories.repository import Repository
from dataloaders.dataloader import DataLoader


ticketController = APIRouter(prefix="/tickets")
ticketRepository = Repository(idSeed=50100)
ticketService = Service[Ticket](ticketRepository)
DataLoader.load(Ticket, ticketRepository, "./dataloaders/data/Tickets.csv")


@ticketController.post("/", status_code=201)
async def post(ticketDTO: TicketDTO) -> Ticket:
    try:
        return ticketService.create(ticketDTO)
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"{error}")


@ticketController.get("/{id}", status_code=200)
async def get(id: int) -> Ticket:
    try:
        return ticketService.getById(id)
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"{error}")


@ticketController.get("/", status_code=200)
async def getAll() -> Iterable[Ticket]:
    try:
        return ticketService.getAll()
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"{error}")


@ticketController.delete("/{id}", status_code=204)
async def delete(id: int) -> None:
    try:
        ticketService.remove(id)
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"{error}")
