# -*- coding: utf-8 -*-
from coppyr.error import CoppyrError


class CoppyrWebError(CoppyrError):
    code = 500

    def to_dict(self):
        result = super().to_dict()
        result.update(code=self.code)
        return result


def multidict_to_dict(multidict):
    """
    Takes a Werkzeug.Multidict and converts it to a regular dict.

    http://werkzeug.pocoo.org/docs/0.12/datastructures/#werkzeug.datastructures.MultiDict

    Note: In newer versions of Werkzeug this converter might be unnecessary.
    """
    return {
        k: multidict.getlist(k)[0] if len(multidict.getlist(k)) == 1
        else multidict.getlist(k)
        for k in multidict.keys()
    }


def strip_parser_none(kwargs):
    """
    Helper to remove all "None" values from a reqparser.parse_args().

    Note: This helper leverages pass by reference in order to communicate
    results to calling context.
    """
    _ = []
    for k, v in kwargs.items():
        if v is None:
            _.append(k)
    for k in _:
        del kwargs[k]
