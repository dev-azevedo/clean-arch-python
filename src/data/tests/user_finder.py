class UserFinderSpy:
    def __init__ (self) -> None:
        self.find_attributes = {}
    
    def find(self, first_name: str) -> dict:
        self.find_attributes["first_name"] = first_name
        
        return {
            "type": "Users",
            "count": 6,
            "attributes": [
                {
                    "first_name": first_name,
                    "last_name": "Doe",
                    "age": 30
                }
            ]
        }