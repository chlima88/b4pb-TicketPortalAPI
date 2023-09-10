from typing import Annotated, Optional, Union

from pydantic import AfterValidator, BaseModel, BeforeValidator, ConfigDict, Field


def isPositive(num: int):
    assert num >= 0, f"{num} deve ser positivo"
    return num


ValidId = Annotated[int, BeforeValidator(isPositive)]


class UserDTO(BaseModel):
    name: str
    role: str
    email: str
    departmentId: int = 0

    model_config = ConfigDict(str_min_length=1, str_strip_whitespace=True)


class User(UserDTO):
    id: ValidId
    isActive: int = 1
