import requests


class TestBase:
    environment_adapter = None
    environment = None
    variables = None
    response = None
    errors = None
    path = None

    def __init__(self, environment_adapter):
        self.environment_adapter = environment_adapter
        self.environment = environment_adapter.get()
        self.variables = self.environment["variables"]

    def request(self):
        self.response = requests.request(
            method="GET", url=self.environment["host"] + self.path, headers=self.environment["headers"])
        return self

    def get_errors(self):
        return self.errors

    def get_json(self):
        return self.response.json()

    def get_json_result(self):
        return self.get_json()["result"]

    def set_variables(self, variables):
        if not self.variables:
            self.variables = {}
        for variable in variables:
            key = self.__class__.__name__
            if key not in self.variables:
                self.variables[key] = {}
            self.variables[key][list(variable.keys()).pop()] = list(
                variable.values()).pop()
        self.environment["variables"] = self.variables
        return self

    def assert_set_variables(self):
        return self

    def print_json_response(self):
        print(self.response.json())

    def test(self):
        assert self.response.status_code == 200
        return self

    def rewrite_token(self):
        self.environment_adapter.set_token(self.get_json())
        return self

    def rewrite_environment(self):
        self.environment_adapter.set(self.environment).write()
        return self
