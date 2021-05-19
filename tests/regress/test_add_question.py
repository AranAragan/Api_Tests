from tests import test_base
import requests


class TestAddQuestion(test_base.TestBase):
    path = "/question"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "product_id": "24617",
                "user_name": "Test",
                "user_email": "test1101111@yandex.ru",
                "text": "Идеально сочный?"
            })
        return self
