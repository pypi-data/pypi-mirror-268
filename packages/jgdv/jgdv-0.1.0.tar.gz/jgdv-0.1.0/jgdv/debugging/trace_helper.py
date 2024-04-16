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

import sys
import trace

class TraceHelper:
    """ Utility to simplify using the trace library, as a context manager

      see https://docs.python.org/3/library/trace.html
    """
    def __init__(self):
        self._tracer = trace.Trace(ignoredirs=[sys.exec_prefix], count=1, countfuncs=0, countcallers=0)
        self._results = None
        self._write_to = None

    def __enter__(self) -> Any:
        #return self
        return

    def __exit__(self, exc_type, exc_value, exc_traceback) -> bool:
        self._results = self._tracer.results()
        if self._write_to:
            self._results.write_results(summary=True, show_missing=True, coverdir=self._write_to)
       # return False to reraise errors
        return

    def this(self, func):
        """ Run a Trace on the passed in function """
        self.runfunc(func)
