from typing import Annotated, Optional, Union

from pydantic import AfterValidator, BaseModel


def isPositive(num: int):
    assert num >= 0, f"{num} deve ser positivo"
    return num


ValidId = Annotated[int, AfterValidator(isPositive)]


class Department(BaseModel):
    id: ValidId
    name: str
    managerId: ValidId


class DepartmentDTO(Department):
    id: Optional[int] = None
