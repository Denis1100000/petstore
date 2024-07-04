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


@allure.suite("Тесты на проверку метода POST /user")
@allure.sub_suite("Позитивные тесты")
@allure.severity(allure.severity_level.BLOCKER)
class TestPostUser:
    @allure.title("Проверка регистрации пользователя")
    def test_post_user(self):
        api = Facade()

        with allure.step("Регистрация нового пользователя"):
            json = UserModel(
                id=2,
                username='user1',
                firstName='firstName',
                lastName='lastName',
                email='test@test.ru',
                password='password',
                phone='+79260000001',
                userStatus=1
            )
            response = api.user_api.post_user(json=json)
        with allure.step("Проверка полученного ответа"):
            assert_that(response, has_properties(
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


