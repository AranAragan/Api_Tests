from tests import test_base
import requests


class TestReviewComment(test_base.TestBase):
    path = "/review/comment"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "product_id": "748",
                "entity_id": "111",
                "user_name": "testo",
                "user_email": "test1101111@yandex.ru",
                "text": "Test"
            })
        return self
