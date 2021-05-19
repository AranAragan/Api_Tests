from tests import test_base
import requests


class TestOrderOneclick(test_base.TestBase):
    path = "/order/oneclick"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "product_id": "622759",
                "phone_number": "79996666666"
            })
        return self
