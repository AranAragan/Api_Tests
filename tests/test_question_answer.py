from tests import test_base
import requests


class TestQuestionAnswer(test_base.TestBase):
    path = "/question/answer"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "product_id": "748",
                "entity_id": "Testo666",
                "user_name": "Testo",
                "user_email": "test1101111@yandex.ru",
                "text": "Test"
            })
        return self
