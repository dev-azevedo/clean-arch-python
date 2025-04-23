from src.domain.user_cases.user_finder import UserFinder as IUserFinder
from src.data.interfaces.users_repository import IUsersRepository
from src.domain.models.users import Users
from src.errors.types import HttpBadRequestError, HttpNotFoundError

class UserFinder(IUserFinder):
    def __init__(self, users_repository: IUsersRepository) -> None:
        self.__users_repository = users_repository
    
    def find(self, first_name: str) -> dict: 
        self.__validade_name(first_name)
        
        users =self.__serch_user(first_name)
        
        response = self.__format_response(users)
        
        return response       
    
    @classmethod
    def __validade_name(cls, first_name: str) -> None:
        if not first_name.isalpha():
            raise HttpBadRequestError("First name must be a string")
        
        if len(first_name) > 18:
            raise HttpBadRequestError("First name must be less than 18 characters")
        
    def __serch_user(self, first_name: str) -> list[Users]:
        users = self.__users_repository.select_user(first_name)
        if len(users) == 0: raise HttpNotFoundError("User not found")
        return users
    
    @classmethod
    def __format_response(cls, users: list[Users]) -> dict:
        attributes = []
        
        for user in users:
            attributes.append({
                "first_name": user.first_name,
                "age": user.age
            })
        
        response = {
            "type": "Users",
            "count": len(attributes),
            "attributes": attributes
        }
        
        return response