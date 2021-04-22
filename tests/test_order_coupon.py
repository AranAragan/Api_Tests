from tests import test_base
import requests


class TestOrderCoupon(test_base.TestBase):
    path = "/order/coupon/SL-4JPWV-18GVF9B"

    def request(self):
        self.response = requests.request(
            method="PUT", url=self.environment["host"] + self.path, headers=self.environment["headers"], data={
            })
        return self
