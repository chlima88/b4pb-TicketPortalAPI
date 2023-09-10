from datetime import datetime
from typing import Annotated, Optional, Union

from pydantic import AfterValidator, BaseModel, BeforeValidator


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


class Ticket(BaseModel):
    id: ValidId
    title: str
    description: str
    statusId: int
    priorityId: int
    createdAt: ValidDateTime
    closedAt: ValidDateTime = ""
    assetId: int = None
    requesterId: int
    attendantId: int = None


class TicketDTO(Ticket):
    id: Optional[int] = None
