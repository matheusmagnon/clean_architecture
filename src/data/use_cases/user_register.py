# pylint: disable=broad-exception-raised

from typing import Dict
from src.domain.use_cases.user_register import UserRegister as UserRegisterInterface
from src.data.interfaces.user_repository import UsersRepositoryInterface
from src.errors.types import HttpBadRequestError


class UserRegister(UserRegisterInterface):

    def __init__(self, user_repository: UsersRepositoryInterface) -> None:
        self.user_repository = user_repository

    def register(self, first_name: str, last_name: str, age: int) -> Dict:
        self.__validate_name(first_name)
        self.__validate_name(last_name)

        self.__registry_user_information(first_name, last_name, age)
        response = self.__format_reponse(first_name, last_name, age)
        return response

    @classmethod
    def __validate_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise HttpBadRequestError('Nome inválido para o cadastro')

        if len(first_name) > 18:
            raise HttpBadRequestError('Nome muito grande para busca')

    def __registry_user_information(self, first_name: str, last_name: str, age: int) -> None:
        self.user_repository.insert_user(first_name, last_name, age)

    @classmethod
    def __format_reponse(cls, first_name: str, last_name: str, age: int) -> Dict:
        response = {
            "type": "Users",
            "count": 1,
            "attributes": {
                "first_name": first_name,
                "last_name": last_name,
                "age": age
            }
        }
        return response
