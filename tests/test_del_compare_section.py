from tests import test_base
import requests


class TestDelCompareSection(test_base.TestBase):
    path = "/compare/section/598682/598682"

    def request(self):
        self.response = requests.request(
            method="DELETE", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        return self
