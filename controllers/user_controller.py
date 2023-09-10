from typing import Iterable
from fastapi import APIRouter

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
    return userService.create(userDTO)


@userController.get("/{id}", status_code=200)
async def get(id: int) -> User:
    return userService.getById(id)


@userController.get("/", status_code=200)
async def getAll() -> Iterable[User]:
    return userService.getAll()


@userController.delete("/{id}", status_code=204)
async def delete(id: int) -> None:
    userService.remove(id)
