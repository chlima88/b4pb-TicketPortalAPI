from datetime import datetime
from typing import Annotated, Optional, Union

from pydantic import AfterValidator, BaseModel


def isPositive(num: int):
    assert num >= 0, f"{num} deve ser positivo"
    return num


def convert_str_to_datetime(date: str):
    if not date or date == "0":
        return ""
    elif isinstance(date, datetime):
        return date
    else:
        return datetime.strptime(date, "%d/%m/%Y %H:%M:%S")


ValidId = Annotated[int, AfterValidator(isPositive)]
ValidDateTime = Annotated[Union[datetime, str], AfterValidator(convert_str_to_datetime)]


class Asset(BaseModel):
    id: ValidId
    brand: str
    model: str
    os: str
    ram: int
    ram: int
    storage: int
    hostname: str
    userId: int = None
    lastStartup: ValidDateTime
    lastSync: ValidDateTime = ""
    securityCompliant: int


class AssetDTO(Asset):
    id: Optional[int] = None
