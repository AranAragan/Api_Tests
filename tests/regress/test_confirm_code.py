from tests import test_base
import requests


class TestConfirmCode(test_base.TestBase):
    path = "/register/code/check/111111"
