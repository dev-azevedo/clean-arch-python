from src.validators.user_register_validator import user_register_validator

class MockRequest:
    def __init__(self) -> None:
        self.json = None


def test_user_register_validator():
    print()
    request = MockRequest()
    request.json = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30
    }
    
    user_register_validator(request=request)