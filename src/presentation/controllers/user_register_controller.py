from src.presentation.interfaces.controller import IController
from src.domain.user_cases.user_register import UserRegister as IUserRegister
from src.presentation.htttp_types.http_request import HttpRequest
from src.presentation.htttp_types.http_response import HttpResponse


class UserRegisterController(IController):
    def __init__(self, use_case: IUserRegister) -> None:
        self.__use_case = use_case
        
    def handle(self, request: HttpRequest) -> HttpResponse:
        first_name = request.body["first_name"]
        last_name = request.body["last_name"]
        age = request.body["age"]
        
        response = self.__use_case.register(first_name=first_name, last_name=last_name, age=age)
        
        return HttpResponse(status_code=200, body={"data": response})