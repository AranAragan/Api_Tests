from tests import test_base
import requests


class TestChangePersonalDataUser(test_base.TestBase):
    path = "/user"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "last_name": "Testun",
                "name": "Testor",
                "second_name": "Testonyo",
                "confirm_code": "111111",
                "password": "11111111"
            })
        return self
