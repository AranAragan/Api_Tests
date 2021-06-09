import allure
from faker import Faker
from pathlib import Path
from tests.negative import test_negative_auth_user
from tests.negative import test_negative_register_user
from tests.negative import test_negative_register_code
from environment import yaml_environment


class Test():
    environment_adapter = yaml_environment.yaml_environment(
        "/environment/test_negative_environment.yml")
    faker = Faker()

    @allure.title("Отправка кода подтверждения")
    @allure.description("Отправка кода подтверждения")
    def test_negative_register_code(self):
        test_negative_register_code.TestNegativeRegisterCode(
            self.environment_adapter, self.faker).request().attach().test()

    @allure.title("Регистрация пользователя")
    @allure.description("Регистрация пользователя")
    @allure.severity("Blocker")
    def test_negative_register_user(self):
        test_negative_register_user.TestNegativeRegisterUser(
            self.environment_adapter, self.faker).request().rewrite_token().rewrite_environment().attach().test()

    @allure.title("Аутентификация пользователя")
    @allure.description("Аутентификация пользователя")
    @allure.severity("Blocker")
    def test_negative_auth_user(self):
        test_negative_auth_user.TestNegativeAuthUser(
            self.environment_adapter, self.faker).request().attach().test()
