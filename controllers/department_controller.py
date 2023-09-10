from typing import Iterable
from fastapi import APIRouter

from models.user import User, UserDTO

departmentController = APIRouter(prefix="/departments")

db = []


@departmentController.post("/")
async def post(userDTO: UserDTO) -> User:
    user = User(id=len(db), **userDTO.model_dump())
    db.append(user)
    return user


@departmentController.get("/{id}")
async def get(id: int) -> User:
    return db[id]


@departmentController.get("/")
async def getAll() -> Iterable[User]:
    return db


@departmentController.delete("/{id}")
async def delete(id: int) -> User:
    return db.pop(id)
