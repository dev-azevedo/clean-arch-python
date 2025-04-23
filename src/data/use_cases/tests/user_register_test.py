from src.data.use_cases.user_register import UserRegister
from src.infra.db.tests.users_repository import UsersRepositorySpy


def test_register():
    first_name = "Ola"
    last_name = "Mundo"
    age = 26
    
    repo = UsersRepositorySpy()    
    user_register = UserRegister(users_repository=repo)
    
    response = user_register.register(first_name=first_name, last_name=last_name, age=age)
    
    assert repo.insert_user_attributes['first_name'] == first_name
    assert repo.insert_user_attributes['last_name'] == last_name
    assert repo.insert_user_attributes['age'] == age
    
    assert response["type"] == "Users"
    assert response["count"] == 1
    assert response["attributes"]
    
def test_registrer_first_name_error():
    first_name = "Ola123123"
    last_name = "Mundo"
    age = 26

    repo = UsersRepositorySpy()    
    user_register = UserRegister(users_repository=repo)
    
    try: 
        response = user_register.register(first_name=first_name, last_name=last_name, age=age)
        assert False
    except Exception as e:
        assert str(e) == "First name must be a string"
        