from tests import test_base
import requests


class TestFeedbacksRequest(test_base.TestBase):
    path = "/feedbacks"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "UF_PHONE_NUMBER": "79996666666",
                "UF_ID_PROD_OR_SALE": "24617",
                "UF_USER_NAME": "Test",
                "UF_USER_COMMENTS": "Test",
                "UF_SOURCE": "Test",
                "UF_EMAIL": "test1101111@yandex.ru",
                "UF_USER_NAME": "Test",
                "APPEAL_TYPE": "1"
            })
        return self
