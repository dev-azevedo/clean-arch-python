from .user_finder import UserFinder
from src.infra.db.tests.users_repository import UsersRepositorySpy

def test_find():
    first_name = "John"
    repo = UsersRepositorySpy()
    user_finder = UserFinder(users_repository=repo)
    
    
    response = user_finder.find(first_name=first_name)
    
    assert repo.select_user_attributes['first_name'] == first_name
    
    assert response["type"] == "Users"
    assert response["count"] == 6
    assert response["attributes"] != [] 
    
def test_find_error_in_invalid_first_name():
    first_name = "John123123"
    repo = UsersRepositorySpy()
    user_finder = UserFinder(users_repository=repo)
    try: 
        response = user_finder.find(first_name=first_name)
        assert False
    except Exception as e:
        assert str(e) == "First name must be a string"

def test_find_error_in_long_first_name():
    first_name = "JohnJohnJohnJohnJohnJohnJohnJohnJohnJohnJohnJohnJohnJohnJohnJohn"
    repo = UsersRepositorySpy()
    user_finder = UserFinder(users_repository=repo)
    try: 
        response = user_finder.find(first_name=first_name)
        assert False
    except Exception as e:
        assert str(e) == "First name must be less than 18 characters"
        
def test_find_error_user_not_found():
    class UsersRepositoryError(UsersRepositorySpy):
        def select_user(self, first_name: str):
            return []
    
    first_name = "John"
    repo = UsersRepositoryError()
    user_finder = UserFinder(users_repository=repo)
    try: 
        response = user_finder.find(first_name=first_name)
        assert False
    except Exception as e:
        assert str(e) == "User not found"