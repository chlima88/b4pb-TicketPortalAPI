from typing import Iterable
from fastapi import APIRouter, HTTPException

from models.user import User, UserDTO
from services.service import Service
from repositories.repository import Repository
from dataloaders.dataloader import DataLoader


userController = APIRouter(prefix="/users")
userRepository = Repository()
userService = Service[User](userRepository)
DataLoader.load(UserDTO, userRepository, "./dataloaders/data/Users.csv")


@userController.post("/", status_code=201)
async def post(userDTO: UserDTO) -> User:
    try:
        return userService.create(userDTO)
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"{error}")


@userController.get("/{id}", status_code=200)
async def get(id: int) -> User:
    try:
        return userService.getById(id)
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"{error}")


@userController.get("/", status_code=200)
async def getAll() -> Iterable[User]:
    try:
        return userService.getAll()
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"{error}")


@userController.delete("/{id}", status_code=204)
async def delete(id: int) -> None:
    try:
        userService.remove(id)
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"{error}")
