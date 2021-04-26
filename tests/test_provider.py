from tests import test_base
import requests


class TestProvider(test_base.TestBase):
    path = "/about/provider"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "user_name": "Test",
                "user_phone": "79996666666",
                "user_email": "test1101111@yandex.ru",
                "products_category": "Test",
                "message": "Test",
                "type": "Test"
            })
        return self
