# -*- coding: utf-8 -*-


class DotDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # recursively cast dicts to DotDicts that may have been set by init
        for k, v in self.items():
            if isinstance(v, dict):
                self[k] = DotDict(**v)

    def __getattr__(self, k):
        if k.startswith("__"):
            return super().__getattr__(k)

        return super().get(k)

    def __setattr__(self, k, v):
        if k.startswith("__"):
            return super().__setattr__(k, v)

        super().__setitem__(k, v)

    def __delattr__(self, k):
        super().__delitem__(k)

    def __setitem__(self, k, v):
        # support recursive dot spec
        if isinstance(v, dict) and not isinstance(v, DotDict):
            v = DotDict(**v)

        super().__setitem__(k, v)
