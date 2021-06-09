from tests import test_base
import requests


class TestBonusPhysical(test_base.TestBase):
    path = "/bonus/physical"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "number": "79996666666",
                "password": "12345678"
            })
        return self
