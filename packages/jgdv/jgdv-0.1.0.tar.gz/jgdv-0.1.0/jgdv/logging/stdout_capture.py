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

import contextlib
import io

with contextlib.redirect_stdout(io.StringIO()) as stdout:
     $0


class ColourStripPrintCapture(logmod.Formatter):
    """
      WARNING: MODIFIES builtins.print
      intercept print commands, so they can be logged at DEBUG level
    Force Colour Command codes to be stripped out of a string.
    """

    _default_fmt      = "{asctime} | {shortname:25} | {message}"
    _default_date_fmt = "%Y-%m-%d %H:%M:%S"
    _default_style    = '{'
    _colour_strip     = re.compile(r'\x1b\[([\d;]+)m?')

    def __init__(self, *, fmt=None, record=False):
        """
        Create a formatter given *Brace* style log format
        """
        super().__init__(fmt or self._default_fmt,
                         datefmt=self._default_date_fmt,
                         style=self._default_style)

    def format(self, record):
        result    = super().format(record)
        no_colour = self._colour_strip.sub("", result)
        return no_colour

    @staticmethod
    def capture_printing_to_file(path:str|pl.Path="print.log", *, disable_warning=False):
        """
        Setup a file handler for a separate logger,
        to keep a trace of anything printed.
        Strips colour print command codes out of any string
        printed strings are logged at DEBUG level
        """
        if not disable_warning:
            import warnings
            warnings.warn("Modifying builtins.print", RuntimeWarning)

        import builtins
        oldprint = builtins.print
        file_handler = logmod.FileHandler(path, mode='w')
        file_handler.setLevel(logmod.DEBUG)
        file_handler.setFormatter(ColourStripPrintCapture())

        print_logger = logmod.getLogger('print.intercept')
        print_logger.setLevel(logmod.NOTSET)
        print_logger.addHandler(file_handler)
        print_logger.propagate = False

        @wraps(oldprint)
        def intercepted(*args, **kwargs):
            """ Wraps `print` to also log to a separate file """
            oldprint(*args, **kwargs)
            if bool(args):
                print_logger.debug(args[0])

        builtins.print = intercepted

    @staticmethod
    def redirect_printing_to_logging(*, disable_warning=False):
        """ redirect printing into logging the logging system to handle
          logged at DEBUG level
        """
        if not disable_warning:
            import warnings
            warnings.warn("Modifying builtins.print", RuntimeWarning)

        import builtins
        oldprint = builtins.print
        print_logger = logmod.getLogger('print.intercept')
        print_logger.setLevel(logmod.DEBUG)

        @wraps(oldprint)
        def intercepted(*args, **kwargs):
            """ Wraps `print` to also log to a separate file """
            oldprint(*args, **kwargs)
            if bool(args):
                print_logger.debug(args[0])

        builtins.print = intercepted
