from tests import test_base
import requests


class TestOrderCoupon(test_base.TestBase):
    path = "/order/coupon/vigodno10"

    def request(self):
        self.response = requests.request(
            method="PUT", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
            })
        return self
