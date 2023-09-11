import os
from typing import Iterable
from fastapi import APIRouter, HTTPException

from models.asset import Asset, AssetDTO
from services.service import Service
from repositories.repository import Repository
from dataloaders.dataloader import DataLoader


assetController = APIRouter(prefix="/assets", tags=["assets"])
assetRepository = Repository()
assetService = Service[Asset](assetRepository)
DataLoader.load(Asset, assetRepository, "Assets.csv")


@assetController.post("/", status_code=201)
async def post(assetDTO: AssetDTO) -> Asset:
    try:
        return assetService.create(assetDTO)
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"{error}")


@assetController.get("/{id}", status_code=200)
async def get(id: int) -> Asset:
    try:
        return assetService.getById(id)
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"{error}")


@assetController.get("/", status_code=200)
async def getAll() -> Iterable[Asset]:
    try:
        return assetService.getAll()
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"{error}")


@assetController.delete("/{id}", status_code=204)
async def delete(id: int) -> None:
    try:
        assetService.remove(id)
    except Exception as error:
        raise HTTPException(status_code=400, detail=f"{error}")
