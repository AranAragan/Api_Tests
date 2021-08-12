from tests import test_base
import requests


class TestDeleteUser(test_base.TestBase):
    path = "/service/delete/users/79996666666?access_token=b0e90087-f447-11eb-9c0e-f2dfe89e1ff8"

    def request(self):
        self.response = requests.request(
            method="GET", url=self.environment["host"] + self.path)
        return self
