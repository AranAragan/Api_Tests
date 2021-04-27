from tests import test_base
import requests


class TestReviewDislike(test_base.TestBase):
    path = "/review/dislike/111?show_entity=возврат_объекта"

    def request(self):
        self.response = requests.request(
            method="PUT", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        return self
