import yaml


class yaml_environment:
    filename = None
    environment = None

    def __init__(self, filename):
        self.filename = filename
        self.environment = self.__read()

    def __read(self):
        with open(self.filename, 'r') as stream:
            return yaml.safe_load(stream)

    def get(self):
        return self.environment

    def set(self, environment):
        self.environment = environment
        return self

    def set_token(self, result):
        try:
            token = result["result"]
            self.environment["access_token"] = token["access_token"]
            self.environment["refresh_token"] = token["refresh_token"]
            self.environment["headers"] = {"Authorization": "Bearer {access_token}".format(
                access_token=token["access_token"])}
        except:
            return self
        return self

    def write(self):
        with open(self.filename, 'w') as stream:
            yaml.dump(self.environment, stream)
