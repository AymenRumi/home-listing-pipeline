import boto3


class SecretsManager:
    def __init__(self, dev: bool = False):

        if dev:
            self.__place_secrets()

    def __place_secrets(self):
        pass

    def read_secrets(self):
        pass

    def _set_env_variables(self):
        pass

