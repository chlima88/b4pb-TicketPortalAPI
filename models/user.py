from typing import Annotated, Optional

from pydantic import AfterValidator, BaseModel, BeforeValidator


def isPositive(num: int):
    assert num >= 0, f"{num} deve ser positivo"
    return num


ValidId = Annotated[int, BeforeValidator(isPositive)]


class UserDTO(BaseModel):
    id: Optional[int] = None
    name: str
    role: str
    email: str
    departmentId: int


class User(UserDTO):
    id: ValidId
    isActive: int = 1
