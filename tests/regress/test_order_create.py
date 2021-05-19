from tests import test_base
import requests


class TestOrderCreate(test_base.TestBase):
    path = "/order/create"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "ORDER_PROP_1": "TEST",
                "ORDER_PROP_2": "test1101111@yandex.ru",
                "ORDER_PROP_7": "TEST",
                "ORDER_PROP_3": "79996666666"
            })
        return self

    def assert_set_variables(self):
        self.set_variables([
            {'ORDER_ID': self.get_json_result()["ORDER_ID"]}
        ])
        return self
