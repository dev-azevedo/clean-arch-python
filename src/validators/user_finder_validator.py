from cerberus import Validator

from src.errors.types import HttpUnprocessableEntityError

def user_finder_validator(request: any):
    body_validator = Validator({
        "first_name": {"type": "string", "required": True, "empty": False, "minlength": 1, "maxlength": 18},
    })
    
    response = body_validator.validate(request.args)
    
    if response is False:
        raise HttpUnprocessableEntityError(body_validator.errors)