#!/usr/bin/env python3
"""

See EOF for license/metadata/notes as applicable
"""

##-- builtin imports
from __future__ import annotations

# import abc
import datetime
import enum
import functools as ftz
import itertools as itz
import logging as logmod
import pathlib as pl
import re
import time
import types
import weakref
# from copy import deepcopy
# from dataclasses import InitVar, dataclass, field
from typing import (TYPE_CHECKING, Any, Callable, ClassVar, Final, Generic,
                    Iterable, Iterator, Mapping, Match, MutableMapping,
                    Protocol, Sequence, Tuple, TypeAlias, TypeGuard, TypeVar,
                    cast, final, overload, runtime_checkable, Generator)
from uuid import UUID, uuid1

##-- end builtin imports

##-- lib imports
import more_itertools as mitz
##-- end lib imports

##-- logging
logging = logmod.getLogger(__name__)
##-- end logging

from time import sleep
import timeit
import time
from random import random

autorange_fmt : Final[str] = "%-*10s : %-*5d calls took: %-*8.2f seconds"
result_fmt    : Final[str] = "Attempt %-*5d : %-*8.2f seconds"
block_fmt     : Final[str] = "%-*10s : %-*8.2f seconds"
once_fmt      : Final[str] = "%-*10s : %-*8.2f seconds"

class JGDVTimer:
    """ Utility Class to time code execution.

      see https://docs.python.org/3/library/timeit.html
    """

    def __init__(self, count=10, repeat=5, keep_gc=False, group:None|str=None):
        self.level            = level
        self.count            = count
        self.repeat           = repeat
        self.keep_gc          = keep_gc
        self.group : str      = f"{group}::" if group else ""
        self.total            = 1.0
        self.once_log         = []

    def msg(self, str, *args):
        logging.debug(str, *args)

    def _set_name(self, name, stmt):
        match name, stmt:
            case str(), _:
                self.current_name = self.group + name
            case _:
                self.current_name = self.group + stmt.__qualname__

    def autorange_cb(self, number, took):
        self.msg(autorange_fmt, self.current_name, number, took)
        self.total += took

    def auto(self, stmt, name=None):
        self._set_name(name, stmt)
        self.msg("-- Autoranging: %s", self.current_name")
        timer = timeit.Timer(stmt, globals=globals())
        timer.autorange(self.autorange_cb)

    def repeats(self, stmt, name=None):
        self._set_name(name, stmt)
        self.msg("-- Repeating %s : Timing %s repeats of %s trials", self.current_name, self.repeat, self.count)
        timer  = timeit.Timer(stmt, globals=globals())
        results = timer.repeat(repeat=self.repeat, number=self.count)
        for i, result in enumerate(results):
            self.msg(result_fmt, i, result)

    def block(self, stmt, name=None):
        self._set_name(name, stmt)
        self.msg("-- Running Block %s : Timing block of %-*5f trials", self.current_name, self.count)
        timer  = timeit.Timer(stmt, globals=globals())
        result = timer.timeit(self.count)
        self.msg(block_fmt, self.current_name, result)

    def once(self, stmt, name=None):
        self._set_name(name, stmt)
        self.msg("-- Running Call Once: %s", self.current_name)
        timer  = timeit.Timer(stmt, globals=globals())
        result = timer.timeit(1)
        self.once_log.append((self.current_name, result))
        self.msg(once_fmt, self.current_name, result)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.msg("-- Finished %s : %-*8.2f", self.group, self.total)
        if self.once_log:
            self.msg("-- Largest Single Call: %s", max(self.once_log, key=lambda x: x[1]))

        return
