class UserRegisterSpy:
    def register(self, first_name: str, last_name: str, age: int) -> dict:
        response = {
            "type": "Users",
            "count": 1,
            "attributes": {
                "first_name": first_name,
                "last_name": last_name,
                "age": age
            }
        }
         
        return response