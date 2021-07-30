from tests import test_base
import requests


class TestDelBasketProductId(test_base.TestBase):
    path = "/basket/638805?total=1"

    def request(self):
        self.response = requests.request(
            method="DELETE", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
            })
        return self
