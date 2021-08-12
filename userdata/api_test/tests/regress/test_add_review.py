from tests import test_base
import requests


class TestAddReview(test_base.TestBase):
    path = "/review"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "product_id": self.environment["custom_variables"]["product_id"],
                "product_rate": "5",
                "advantages": "Сочный",
                "limitations": "Не сочный",
                "text": "Идеально сочный",
                "user_email": self.environment["custom_variables"]["user_email"],
                "user_name": self.environment["custom_variables"]["user_name"]
            })
        return self
