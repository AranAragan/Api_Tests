from tests import test_base
import requests


class TestReviewProduct(test_base.TestBase):
    path = "/review"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "product_id": "24617",
                "product_rate": "5",
                "advantages": "Сочный",
                "limitations": "Не сочный",
                "text": "Идеально сочный",
                "user_email": "test1101111@yandex.ru",
                "user_name": "TEST"

            })
        return self
