from tests import test_base
import requests


class TestRecommendDeveloper(test_base.TestBase):
    path = "/about/recommend/developer"

    def request(self):
        self.response = requests.request(
            method="POST", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
                "user_name": "Test",
                "user_phone": "79996666666",
                "user_email": "test1101111@yandex.ru",
                "candidate_profile": "www.05.ru",
                "candidate_name": "Test",
                "candidate_phone": "79996666666"
            })
        return self
