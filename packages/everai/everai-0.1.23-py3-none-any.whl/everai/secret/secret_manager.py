from everai.secret import Secret
import os
from pathlib import Path
from everai.token_manager import TokenManager
from everai.api import API
from generated.secrets import V1Secret
import base64


class SecretManager:
    def __init__(self):
        self.api = API()

    def create(self, name: str, data: dict[str, str]) -> Secret:
        secret = Secret(name=name, data=data)
        v1secret = secret.to_proto()
        resp = self.api.create_secret(v1secret)
        return Secret.from_proto(resp)

    def create_from_lines(self, name: str, lines: list[str]) -> Secret:
        data: dict[str, str] = {}

        for line in lines:
            key_value = line.split('=', 1)

            if len(key_value) == 2:
                data[key_value[0]] = key_value[1]
            else:
                data[key_value[0]] = ''
        return self.create(name, data)

    def create_from_file(self, name: str, file: str) -> Secret:
        lines: list[str] = []

        with open(file, "r") as f:
            lines = f.readlines()
            return self.create_from_lines(name, lines)

    def delete(self, name: str):
        self.api.delete_secret(name)

    def list(self) -> list[Secret]:
        resp = self.api.list_secrets()

        list_secrets: list[Secret] = []
        for v1secret in resp:
            list_secrets.append(Secret.from_proto(v1secret))

        return list_secrets

    def get(self, name: str) -> Secret:
        resp = self.api.get_secret(name)
        return Secret.from_proto(resp)
