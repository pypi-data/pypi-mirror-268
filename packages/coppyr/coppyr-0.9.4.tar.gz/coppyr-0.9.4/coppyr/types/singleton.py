# -*- coding: utf-8 -*-
from coppyr.collections import DotDict


class Singleton(object):
    """
    This object will only ever create one instance of itself in (interpreter
    local) memory.  Future constructions will just return the previously
    constructed instance.

    WARNING: Since construction is separate from initialization (__new__
    vs. __init__), it is possible that the __init__ method can inadvertantly be
    called multiple times for a single instance.  While new will return the
    previously instantiated object, the interpreter will flow through __init__
    as if it had just constructed a fresh object.
    """
    _instance = None
    _init = True  # use this flag to skip future init calls if desirable

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._init = False


class Namespace(Singleton, DotDict):
    """
    Simple object that acts as a an easily shared variable store.
    """

    def __init__(self, *args, **kwargs):
        if not self._init:
            return

        super().__init__(*args, **kwargs)
