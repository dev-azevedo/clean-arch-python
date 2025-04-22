from src.domain.models.users import Users

class UsersRepositorySpy:
    def __init__(self) -> None:
        self.insert_user_attributes = {}
        self.select_user_attributes = {}
        
    def insert_user(self, first_name: str, last_name: str, age: int) -> None:
        self.insert_user_attributes["first_name"] = first_name
        self.insert_user_attributes["last_name"] = last_name
        self.insert_user_attributes["age"] = age
        
    def select_user(self, first_name: str) -> list[Users]:
        self.select_user_attributes["first_name"] = first_name
        return [
            Users(id=1, first_name="John", last_name="Doe", age=30),
            Users(id=2, first_name="John2", last_name="Doe2", age=32),
            Users(id=3, first_name="John3", last_name="Doe3", age=33),
            Users(id=4, first_name="John4", last_name="Doe4", age=34),
            Users(id=5, first_name="John5", last_name="Doe5", age=35),
            Users(id=6, first_name="John6", last_name="Doe6", age=36)
        ]
