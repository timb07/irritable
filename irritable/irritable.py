# -*- coding: utf-8 -*-

import random
from itertools import tee

__all__ = [
    'StopIrritation',
    'irrit',
]


class StopIrritation(Exception):
    pass


class BaseIrritator:
    def __init__(self, iterator):
        self.iterator = iterator

    def __iter__(self):
        return self


class Irritator(BaseIrritator):
    stop = False
    repeat = None

    def __init__(self, *args, resume=False, repeat=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.resume = 0.95 if resume else False
        if repeat:
            self.iterator, self.repeat = tee(self.iterator)

    def __next__(self):
        if self.resume:
            self._stop_or_resume()
        try:
            return next(self.iterator)
        except StopIteration:
            if not self.stop:
                self.stop = True
                raise
            else:
                if self.repeat is not None:
                    return self._repeat()
                raise StopIrritation('StopIteration has already been raised')

    def _stop_or_resume(self):
        if random.random() > self.resume:
            self.resume = False
            raise StopIteration
        else:
            self.resume *= 0.95

    def _repeat(self):
        self.iterator, self.repeat = tee(self.repeat)
        self.stop = False
        return next(self.iterator)


def irrit(iterable, **kwargs):
    return Irritator(iter(iterable), **kwargs)
