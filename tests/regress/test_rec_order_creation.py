from tests import test_base
import requests


class TestRecOrderCreation(test_base.TestBase):
    path = "/order"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "ORDER_PROP_1": "TEST",
                "ORDER_PROP_2": "test1101111@yandex.ru",
                "ORDER_PROP_7": "TEST",
                "ORDER_PROP_3": "TEST"
            })
        return self
