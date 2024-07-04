from petstore_user.apis.user_api import UserApi
from config import API_HOST


class Facade:
    def __init__(self, host: str = API_HOST):
        self.user_api = UserApi(host)
