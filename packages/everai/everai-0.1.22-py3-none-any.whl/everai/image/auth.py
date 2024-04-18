import typing
from abc import ABC, abstractmethod


class Auth(ABC):
    @abstractmethod
    def authenticate(self):
        raise NotImplementedError


ARG_TYPE = typing.Union[str, typing.Callable[[], str]]


class BasicAuth(Auth):
    username: ARG_TYPE
    password: ARG_TYPE

    def __init__(self, username: ARG_TYPE, password: ARG_TYPE):
        self.username = username
        self.password = password

    def authenticate(self):
        return self.username, self.password
