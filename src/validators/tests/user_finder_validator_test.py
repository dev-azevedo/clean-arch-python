from src.validators.user_finder_validator import user_finder_validator

class MockRequest:
    def __init__(self) -> None:
        self.args = None


def test_user_finder_validator():
    print()
    request = MockRequest()
    request.args = {
        "first_name": "John",
    }
    
    user_finder_validator(request=request)