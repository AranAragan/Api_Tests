from tests import test_base
import requests


class TestRegisterUser(test_base.TestBase):
    path = "/register"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "name": "TEST",
                "last_name": "TESTOV",
                "second_name": "TESTOVICH",
                "confirm_code": "111111",
                "password": "111111",
                "email": "test1101111@yandex.ru"
            })
        return self
