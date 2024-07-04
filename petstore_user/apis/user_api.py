from requests import Response, session
from ..models import *
from ..utilities import validate_request_json, validate_status_code
from client.restclient import RestClient


class UserApi:
    def __init__(self, host):
        self.host = host
        self.client = RestClient(host=host)

    def post_user(self, json: UserModel, status_code: int = 200, **kwargs) -> Response | ApiResponse:
        response = self.client.post(
            path='/user',
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return ApiResponse(**response.json())
        return response

    def get_user_login(self, params: dict, status_code: int = 200, **kwargs) -> Response | ApiResponse:
        response = self.client.get(
            path=f'/user/login',
            params=params,
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return ApiResponse(**response.json())
        return response

    def put_user(self, username: str, json: UserModel, status_code: int = 200,
                 **kwargs) -> Response | ApiResponse:
        response = self.client.put(
            path=f'/user/{username}',
            json=validate_request_json(json),
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return ApiResponse(**response.json())
        return response

    def delete_user(self, username: str, status_code: int = 200, **kwargs) -> Response | ApiResponse:
        response = self.client.delete(
            path=f'/user/{username}',
            **kwargs
        )
        validate_status_code(response, status_code)
        if response.status_code == 200:
            return ApiResponse(**response.json())
        return response
