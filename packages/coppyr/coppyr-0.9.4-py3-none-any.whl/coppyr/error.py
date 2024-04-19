# -*- coding: utf-8 -*-
import json
from typing import Type


class CoppyrError(Exception):
    """
    Simple base exception to provide boiler plate for readable, consistent
    error messages.  Also has a dict representation for easy(ish) conversion to
    JSON for web use cases.

    Provides some basic extensions and representation handling.
    """

    description = "Something unexpected happened."

    def __init__(self, message=None, payload=None, caught=None):
        super().__init__()
        self.message = message if message is not None else self.description
        self.payload = payload if payload is not None else {}

        if caught is not None:
            self.payload.update({
                "caught": {
                    "name": caught.__class__.__name__,
                    "message": getattr(caught, "message", str(caught)),
                }
            })

    def to_dict(self):
        return {
            "error": self.__class__.__name__,
            "message": self.message,
            "payload": self.payload if self.payload is not None else {}
        }

    def to_json(self, indent=None):
        return json.dumps(self.to_dict(), indent=indent)

    def __repr__(self):
        return f"{self.__class__.__name__}"\
               f"(message={self.message}, payload={self.payload})"

    def __str__(self):
        return self.message


def exc_formatter(
    e: Exception,
    coerce: bool = False,
    cls: Type[CoppyrError] = CoppyrError
):
    if coerce:
        e = cls(caught=e)

    import sys
    _, _, tb = sys.exc_info()

    error_with_tb = e.with_traceback(tb)
    return error_with_tb
