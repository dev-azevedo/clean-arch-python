from cerberus import Validator

from src.errors.types import HttpUnprocessableEntityError

def user_register_validator(request: any):
    body_validator = Validator({
        "first_name": {"type": "string", "required": True, "empty": False, "minlength": 1, "maxlength": 18},
        "last_name": {"type": "string", "required": True, "empty": False, "minlength": 1, "maxlength": 18},
        "age": {"type": "integer", "required": True, "empty": False, "min": 0, "max": 100}
    })
    
    response = body_validator.validate(request.json)
    
    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)