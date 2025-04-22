from src.domain.user_cases.user_register import UserRegister as IUserRegister
from src.data.interfaces.users_repository import IUsersRepository
class UserRegister(IUserRegister):
    def __init__(self, users_repository: IUsersRepository) -> None:
        self.__users_repository = users_repository
    
    def register(self, first_name: str, last_name: str, age: int) -> dict:
        self.__validade_name(first_name)
        self.__validade_name(last_name)
        self.__registry_user_information(first_name=first_name, last_name=last_name, age=age)
        
        response = self.__format_response(first_name=first_name, last_name=last_name, age=age)
        
        return response
    
     
    @classmethod
    def __validade_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise Exception("First name must be a string")
        
        if len(first_name) > 18:
            raise Exception("First name must be less than 18 characters")
        
    def __registry_user_information(self, first_name: str, last_name: str, age: int) -> None:
        self.__users_repository.insert_user(first_name=first_name, last_name=last_name, age=age)
    
    @classmethod
    def __format_response(cls, first_name: str, last_name: str, age: int) -> dict:
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
        