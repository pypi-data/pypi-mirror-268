from everai.app import context


class Placeholder:
    def __init__(self, secret_name: str, secret_key: str):
        self.secret_name = secret_name
        self.secret_key = secret_key

    def __call__(self) -> str:
        secret = context.get_secret(self.secret_name)
        assert secret is not None

        secret_value = secret.get(self.secret_key)
        assert secret_value is not None

        return secret_value
