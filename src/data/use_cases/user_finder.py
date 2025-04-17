from src.domain.user_cases.user_finder import UserFinder as IUserFinder
from src.data.interfaces.users_repository import UsersRepository as IUsersRepository

class UserFinder(IUserFinder):
    def __init__(self, users_repository: IUsersRepository) -> None:
        self.__users_repository = users_repository
    
    def find(self, first_name: str) -> dict: pass  
