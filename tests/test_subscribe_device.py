from tests import test_base
import requests


class TestSubscribeDevice(test_base.TestBase):
    path = "/events/subscribe/1a418dbe-b9f3-11ea-a96b-b42e9981f624"

    def request(self):
        self.response = requests.request(
            method="PUT", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        return self
