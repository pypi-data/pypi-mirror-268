from typing import Any


class SanetError(Exception):
    pass


class SanetResponseError(SanetError):
    def __init__(self, message: str, response: Any = None):
        super().__init__(message, response)
        self.message = message
        self.response = response
