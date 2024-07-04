import structlog
from services.petstore import Facade
from petstore_user.models.user_model import UserModel
from hamcrest import assert_that, has_properties
import allure
import re

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


@allure.suite("Тесты на проверку метода GET /user/login")
@allure.sub_suite("Позитивные тесты")
@allure.severity(allure.severity_level.BLOCKER)
class TestGetUser:
    @allure.title("Проверка авторизации пользователя")
    def test_get_user(self):
        api = Facade()

        with allure.step("Регистрация нового пользователя"):
            json = UserModel(
                id=2,
                username='test1',
                firstName='firstName',
                lastName='lastName',
                email='test@test.ru',
                password='password',
                phone='+79260000001',
                userStatus=1
            )
            register_new_user = api.user_api.post_user(json)
        with allure.step("Проверка полученного ответа"):
            assert_that(register_new_user, has_properties(
                {
                    "code": 200,
                    "type": "unknown",
                    "message": "2"
                }
            ))
        with allure.step("Авторизация пользователя"):
            params = {"username": json.username, "password": json.password}
            get_registered_user = api.user_api.get_user_login(params=params)
        with allure.step("Проверка полученного ответа"):
            assert_that(get_registered_user, has_properties(
                {
                    "code": 200,
                    "type": "unknown"
                }
            ))
            session = get_registered_user.message
            assert re.match(r'logged in user session:\d{13}', session)
        with allure.step("Удаление пользователя"):
            deleted_user = api.user_api.delete_user(username=json.username)
        with allure.step("Проверка полученного ответа"):
            assert_that(deleted_user, has_properties(
                {
                    "code": 200,
                    "type": "unknown",
                    "message": json.username
                }
            ))
