from tests import test_base
import requests


class TestFavoriteProduct(test_base.TestBase):
    path = "/favorite/623277?show_entity=598682"

    def request(self):
        self.response = requests.request(
            method="PUT", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        return self
