import structlog

from services.petstore import Facade
from petstore_user.models.user_model import UserModel
from hamcrest import assert_that, has_properties
import allure

structlog.configure(
    processors=[
        structlog.processors.JSONRenderer(indent=4, sort_keys=True, ensure_ascii=False)
    ]
)


@allure.suite("Тесты на проверку метода PUT /user")
@allure.sub_suite("Позитивные тесты")
@allure.severity(allure.severity_level.BLOCKER)
class TestPutUser:
    @allure.title("Проверка изменения имени пользователя")
    def test_put_user(self):
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

        with allure.step("Изменение имени пользователя"):
            username = 'TEST1'
            json.username = 'TEST1'
            change_username = api.user_api.put_user(json=json, username=username)
        with allure.step("Проверка полученного ответа"):
            assert_that(change_username, has_properties(
                {
                    "code": 200,
                    "type": "unknown",
                    "message": "2"
                }
            ))
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
