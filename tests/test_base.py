import requests


class test_base:
    environment_adapter = None
    environment = None
    response = None
    errors = None
    path = None

    def __init__(self, environment_adapter):
        self.environment_adapter = environment_adapter
        self.environment = environment_adapter.get()

    def request(self):
        self.response = requests.request(
            method="GET", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        return self

    def get_errors(self):
        return self.errors

    def get_json(self):
        return self.response.json()

    def print_json_response(self):
        print(self.response.json())

    def rewrite_token(self):
        self.environment_adapter.set_token(self.get_json()).write()
        return self
