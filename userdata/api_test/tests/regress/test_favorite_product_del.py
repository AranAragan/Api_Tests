from tests import test_base
import requests


class TestFavoriteProductDel(test_base.TestBase):
    path = "/favorite/598680?show_entity=возврат_добавленного_товара"

    def request(self):
        self.response = requests.request(
            method="DELETE", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        return self
