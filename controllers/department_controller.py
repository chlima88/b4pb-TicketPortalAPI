from typing import Iterable
from fastapi import APIRouter, HTTPException

from models.department import Department, DepartmentDTO
from services.service import Service
from repositories.repository import Repository
from dataloaders.dataloader import DataLoader


departmentController = APIRouter(prefix="/departments", tags=["departments"])
departmentRepository = Repository()
departmentService = Service[Department](departmentRepository)
DataLoader.load(Department, departmentRepository, "Departments.csv")


@departmentController.post("/", status_code=201)
async def post(departmentDTO: DepartmentDTO) -> Department:
    try:
        return departmentService.create(departmentDTO)
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"{error}")


@departmentController.get("/{id}", status_code=200)
async def get(id: int) -> Department:
    try:
        return departmentService.getById(id)
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"{error}")


@departmentController.get("/", status_code=200)
async def getAll() -> Iterable[Department]:
    try:
        return departmentService.getAll()
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"{error}")


@departmentController.delete("/{id}", status_code=204)
async def delete(id: int) -> None:
    try:
        departmentService.remove(id)
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"{error}")
