from src.presentation.controllers.user_finder_controller import UserFinderController
from src.data.tests.user_finder import UserFinderSpy
from src.presentation.htttp_types.http_response import HttpResponse as IHttpResponse

class HttpRequestMock:
    def __init__(self) -> None:
        self.query_params = {"first_name": "John"}


def test_handle():
    http_request_mock = HttpRequestMock()
    use_case = UserFinderSpy()
    user_finder_controller = UserFinderController(use_case=use_case)
    
    response = user_finder_controller.handle(http_request=http_request_mock)
    
    assert isinstance(response, IHttpResponse)
    assert response.status_code == 200
    assert response.body["data"] is not None