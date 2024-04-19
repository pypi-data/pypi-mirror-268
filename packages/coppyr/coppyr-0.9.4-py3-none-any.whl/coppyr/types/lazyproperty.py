# -*- coding: utf-8 -*-


class lazyproperty(object):
    """
    Decorator for creating properties that're only evaluated once.
    """
    def __init__(self, method):
        self.method = method

    def __get__(self, instance, cls):
        value = self.method(instance)
        setattr(instance, self.method.__name__, value)
        return value
