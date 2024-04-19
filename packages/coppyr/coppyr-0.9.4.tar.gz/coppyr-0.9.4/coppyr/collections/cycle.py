# -*- coding: utf-8 -*-


class cycle(object):
    """
    Simple circular buffer generator that doesn't require the storing of a full
    iterable like `collections.cycle`.

    WARNING: This object is an endless generator.  Be careful to not
    boundlessly iterate.
    """
    def __init__(self, start=0, stop=None, step=1):
        if stop is None:
            stop = start
            start = 0

        self.start = start
        self.step = step
        self.stop = stop - self.step
        # to mirror range behavior, we want to stop one step so we never
        # increment to >= stop.

        # init _current to 1 step behind so the first value is the actual
        # start after increment
        self._current = self.start - self.step

    def __iter__(self):
        return self

    def __next__(self):
        # if we aren't at the bound...
        if self._current < self.stop:
            # ...step
            self._current += self.step
        else:
            # we are at the bound...so start over
            self._current = self.start

        return self._current
