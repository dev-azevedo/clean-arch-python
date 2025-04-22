from abc import ABC, abstractmethod
from src.domain.models.users import Users

class IUsersRepository(ABC):
    @abstractmethod
    def insert_user(self, first_name: str, last_name: str, age: int) -> None: pass
    
    @abstractmethod
    def select_user(self, first_name: str) -> list[Users]: pass