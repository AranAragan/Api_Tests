from tests import test_base
import requests


class TestDelCompare(test_base.TestBase):
    path = "/compare/598682"

    def request(self):
        self.response = requests.request(
            method="DELETE", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        return self
