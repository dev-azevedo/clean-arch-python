from .users_repository import UsersRepository

def test_insert_user():
    mocked_first_name = "John"
    mocked_last_name = "Doe"
    mocked_age = 30
    users_repository = UsersRepository()
    users_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)
