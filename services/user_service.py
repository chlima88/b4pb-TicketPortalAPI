from typing import Iterable
from models.user import User, UserDTO
from interfaces.repository_interface import IRepository


class UserService:
    def __init__(self, userRepository: IRepository):
        self.userRepository = userRepository

    def create(self, userDTO: UserDTO) -> User:
        id = self.userRepository.count()
        userDTO.id = id
        user = User(**userDTO.model_dump())
        return self.userRepository.save(user)

    def getAll(self) -> Iterable[User]:
        return self.userRepository.findAll()

    def getById(self, id: int) -> User:
        user = self.userRepository.findById(id)
        return user

    def remove(self, id: int) -> None:
        self.userRepository.deleteById(id)
