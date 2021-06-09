from tests import test_base
import requests


class TestUnsubscribe(test_base.TestBase):
    path = "/events/unsubscribe/1a418dbe-b9f3-11ea-a96b-b42e9981f624"

    def request(self):
        self.response = requests.request(
            method="DELETE", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
            })
        return self
