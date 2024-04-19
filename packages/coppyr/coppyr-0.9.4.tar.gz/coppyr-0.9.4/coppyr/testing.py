# -*- coding: utf-8 -*-
from contextlib import contextmanager


@contextmanager
def expect_exception(exc=Exception):
    """
    Provide context wrapper that wraps code and only passes if the specified
    exception is raised.
    """
    try:
        yield
        assert False  # exception was not raised
    except exc:
        # exception was raised, and we catch it here
        pass
