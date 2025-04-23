from src.presentation.interfaces.controller import IController
from src.domain.user_cases.user_finder import UserFinder as IUserFider
from src.presentation.htttp_types.http_request import HttpRequest
from src.presentation.htttp_types.http_response import HttpResponse


class UserFinderController(IController):
    def __init__(self, use_case: IUserFider) -> None:
        self.__use_case = use_case
        
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        first_name = http_request.query_params["first_name"]
        
        response = self.__use_case.find(first_name=first_name)
        
        return HttpResponse(status_code=200, body={"data": response})