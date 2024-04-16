#!/usr/bin/env python3
"""

"""
##-- imports
from __future__ import annotations

import types
import abc
import datetime
import enum
import functools as ftz
import itertools as itz
import logging as logmod
import pathlib as pl
import re
import time
from copy import deepcopy
from dataclasses import InitVar, dataclass, field
from typing import (TYPE_CHECKING, Any, Callable, ClassVar, Final, Generic,
                    Iterable, Iterator, Mapping, Match, MutableMapping,
                    Protocol, Sequence, Tuple, TypeAlias, TypeGuard, TypeVar,
                    cast, final, overload, runtime_checkable)
from uuid import UUID, uuid1
from weakref import ref

##-- end imports

##-- logging
logging = logmod.getLogger(__name__)
##-- end logging

class VoronoiIO:

    @staticmmethod
    def save_graph(values:np.ndarray, fpath):
        """
        Pickle the voronoi points into a file
        """
        fpath.write_text(pickle.dumps(values)

    @staticmethod
    def load_graph(fpath):
        """
        Load the pickled graph of voronoi points
        """
        return pickle.loads(fpath.read_text())
