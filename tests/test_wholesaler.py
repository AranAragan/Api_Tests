from tests import test_base
import requests


class TestWholesaler(test_base.TestBase):
    path = "/about/wholesaler"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "user_name": "Test",
                "user_phone": "79996666666",
                "city": "Test",
                "products": "test?",
                "products_category": "Test"
            })
        return self
