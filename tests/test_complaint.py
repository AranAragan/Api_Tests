from tests import test_base
import requests


class TestComplaint(test_base.TestBase):
    path = "/complaint"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "product_id": "748",
                "user_name": "Testo",
                "user_email": "test1101111@40yandex.ru",
                "text": "TESTO"
            })
        return self
