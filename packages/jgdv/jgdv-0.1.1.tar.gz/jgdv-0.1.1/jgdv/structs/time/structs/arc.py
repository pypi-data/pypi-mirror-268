"""
Arcs express segments of rational time
"""
##-- imports
from __future__ import annotations

from fractions import Fraction
from .utils import time_str
import logging as root_logger
##-- end imports

logging = root_logger.getLogger(__name__)

class Arc:
    """ A segment of rational time """

    @staticmethod
    def copy(val):
        return Arc(val.start, val.end)

    def __init__(self, a, b):
        assert(isinstance(a, Fraction))
        assert(isinstance(b, Fraction))
        self.start = a
        self.end = b

    def __contains__(self, other):
        """ Test whether the given time is within bounds """
        test = other
        if not isinstance(other, Fraction):
            assert(hasattr(other, 'arc'))
            test = other.arc.start
        assert(isinstance(test, Fraction))
        return self.start <= test and test < self.end

    def __repr__(self):
        """ A Readable format of an arc """
        return f"({time_str(self.start)}..{time_str(self.end)})"

    def __eq__(self, other):
        if not isinstance(other, Arc):
            raise TypeError()

        return all([x == y for x,y in zip(self.pair(), other.pair())])

    def pair(self):
        """ Treat the arc as a list """
        return [self.start, self.end]

    def size(self):
        """ Get the length of time the arc describes """
        return self.end - self.start

    def bound(self, other):
        assert(isinstance(other, Arc))
        start = min(self.start, other.start)
        end = max(self.end, other.end)
        return Arc(start, end)
