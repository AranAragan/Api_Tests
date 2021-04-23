from tests import test_base
import requests


class TestRegBonus(test_base.TestBase):
    path = "/bonus?name=Test&last_name=Testov&second_name=Testovich"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        return self
