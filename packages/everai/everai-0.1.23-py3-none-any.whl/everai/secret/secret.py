from __future__ import annotations

import base64
import json

from generated.secrets import V1Secret


class Secret:
    def __init__(self, name: str, data: dict[str, str]):
        self.name = name or ''
        self.data = data or {}

    def get(self, key: str, default: str | None = None) -> str:
        value = self.data.get(key, None)
        if value is None:
            return default
        return value

    def __show(self) -> str:
        lines: list[str] = [f"Secret(Name: {self.name})"]
        data = {} if self.data is None else self.data

        lines.extend([f'\t{k} - ******' for k in data])

        return '\n'.join(lines) + '\n'

    @staticmethod
    def from_proto(sec: V1Secret) -> Secret:
        plaintext_data = {key: base64.b64decode(value).decode('utf-8')
                          for key, value in sec.data.items()}
        return Secret(name=sec.name, data=plaintext_data)

    def to_proto(self) -> V1Secret:
        base64_dict = {key: base64.b64encode(value.encode('utf-8')).decode('utf-8')
                       for key, value in self.data.items()}
        return V1Secret(name=self.name, data=base64_dict)

    def to_json(self):
        v1secret = self.to_proto()
        json_out_data = {
            'name': self.name,
            'data': v1secret.data
        }
        return json.dumps(json_out_data, ensure_ascii=False)

    def __str__(self):
        return self.__show()

    def __repr__(self):
        return self.__show()
