from abc import ABC, abstractmethod
from typing import dict

class UserFinder(ABC):
    
    @abstractmethod
    def find(self, first_name: str) -> dict: pass