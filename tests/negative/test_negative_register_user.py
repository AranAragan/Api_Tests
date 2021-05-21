from tests import test_base
import requests


class TestNegativeRegisterUser(test_base.TestBase):
    path = "/register"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "name": " ",
                "last_name": " ",
                "second_name": " ",
                "confirm_code": "111111",
                "password": "1",
                "email": "test1101111_yandex.ru"
            })
        return self

    def test(self):
        assert self.response.status_code != 200
        return self
