#!/usr/bin/env python3
"""

"""
##-- imports
from __future__ import annotations

# import abc
# import datetime
import enum
import functools as ftz
import itertools as itz
import logging as logmod
import pathlib as pl
import re
import time
import types
# from copy import deepcopy
# from dataclasses import InitVar, dataclass, field
from typing import (TYPE_CHECKING, Any, Callable, ClassVar, Final, Generic,
                    Iterable, Iterator, Mapping, Match, MutableMapping,
                    Protocol, Sequence, Tuple, TypeAlias, TypeGuard, TypeVar,
                    cast, final, overload, runtime_checkable, Generator, Literal)
# from uuid import UUID, uuid1
# from weakref import ref

# from bs4 import BeautifulSoup
import boltons.queueutils
# import construct as C
# import dirty-equals as deq
# import graphviz
# import matplotlib.pyplot as plt
# import more_itertools as itzplus
import networkx as nx
# import numpy as np
# import pandas
# import pomegranate as pom
# import pony import orm
# import pronouncing
# import pyparsing as pp
# import rich
# import seaborn as sns
# import sklearn
# import stackprinter # stackprinter.set_excepthook(style='darkbg2')
# import sty
# import sympy
# import tomllib
# import toolz
# import tqdm
# import validators
# import z3
# import spacy # nlp = spacy.load("en_core_web_sm")

##-- end imports

##-- logging
logging = logmod.getLogger(__name__)
##-- end logging

from collections import defaultdict
from queue import PriorityQueue
import jgdv
from jgdv.enums.task_state import TaskStateEnum

@jgdv.check_protocol
class JGDVReactorTracker(BaseTracker, TaskTracker_i):
    """
    track dependencies in a networkx digraph,
    successors of a node are its dependencies.
      ie: ROOT -> Task -> Dependency -> SubDependency

    tracks definite and indefinite artifacts as products and dependencies of tasks as well.

    the `task_graph` stores nodes as full names of tasks
    """
    state_e = TaskStateEnum

    def __init__(self, shadowing:bool=False, *, policy=None):
        super().__init__(policy=policy) # self.tasks

    def add_task(self, task:JGDVTaskSpec|TaskBase_i, *, no_root_connection=False) -> None:
        """ add a task description into the tracker, but don't queue it
        connecting it with its dependencies and tasks that depend on it
        """

        task : TaskBase_i = self._prep_task(task)
        assert(isinstance(task, TaskBase_i))
        # Store it
        self.tasks[task.name] = task

        # Insert into dependency graph
        self.task_graph.add_node(task.name, state=self.INITIAL_TASK_STATE, priority=task.spec.priority)

        # Then connect it:
        if not no_root_connection:
            self.task_graph.add_edge(ROOT, task.name)

        self._insert_dependencies(task)
        self._insert_dependents(task)
        self._insert_according_to_queue_behaviour(task)

    def update_state(self, task:str|TaskBase_i|JGDVTaskArtifact, state:self.state_e):
        """ update the state of a task in the dependency graph """
        logging.debug("Updating Task State: %s -> %s", task, state)
        match task, state:
            case str(), self.state_e() if task in self.task_graph:
                self.task_graph.nodes[task]['state'] = state
            case TaskBase_i(), self.state_e() if task.name in self.task_graph:
                self.task_graph.nodes[task.name]['state'] = state
            case JGDVTaskArtifact(), self.state_e() if task in self.task_graph:
                self.task_graph.nodes[task]['state'] = state
            case _, _:
                raise doot.errors.DootTaskTrackingError("Bad task update state args", task, state)

    def next_for(self, target:None|str=None) -> None|Job_i|Task_i:
        """ ask for the next task that can be performed """
        if target and target not in self.active_set:
            self.queue_task(target, silent=True)

        focus : str | JGDVTaskArtifact | None = None
        adj                                   = dict(self.task_graph.adjacency())
        while bool(self.task_queue):
            focus : str = self.task_queue.peek()
            logging.debug("Task: %s  State: %s, Stack: %s", focus, self.task_state(focus), self.active_set)

            if focus in self.task_graph and self.task_graph.nodes[focus][PRIORITY] < self._min_priority:
                logging.warning("Task reached minimum priority while waiting, and has been cancelled: %s", focus)
                self.update_state(focus, self.state_e.FAILED)

            match self.task_state(focus):
                case self.state_e.SUCCESS: # remove task on completion
                    self.deque_task()
                case self.state_e.EXISTS:  # remove artifact when it exists
                    for pred in self.task_graph.pred[focus].keys():
                        logging.debug("Propagating Artifact existence to disable: %s", pred)
                        self.update_state(pred, self.state_e.SUCCESS)
                    self.deque_task()
                    return self.artifacts[focus]
                case self.state_e.HALTED:  # remove and propagate halted status
                    # anything that depends on a halted task in turn gets halted
                    halting = list(self.task_graph.succ[focus].keys())
                    printer.warning("Propagating Halt from: %s to: %s", focus, halting)
                    for pred in halting:
                        self.update_state(pred, self.state_e.HALTED)
                    # And remove the halted task from the active_set
                    self.deque_task()
                case self.state_e.FAILED:  # stop when a task fails, and clear any queued tasks
                    self.clear_queue()
                    return None
                case self.state_e.RUNNING:
                    logging.debug("Got Running Task: %s, continuing", focus)
                case self.state_e.READY if focus in self.execution_path: # error on running the same task twice
                    raise doot.errors.DootTaskTrackingError("Task Attempted to run twice: %s", focus)
                case self.state_e.READY:   # return the task if its ready
                    self.execution_path.append(focus)
                    self.update_state(focus, self.state_e.RUNNING)
                    self.task_graph.nodes[focus][PRIORITY] -= 1
                    return self.tasks.get(focus, None)
                case self.state_e.ARTIFACT if bool(self.artifacts[focus]): # if an artifact exists, mark it so
                    self.update_state(focus, self.state_e.EXISTS)
                case self.state_e.ARTIFACT: # Add dependencies of an artifact to the stack
                    incomplete, all_deps = self._task_dependencies(focus)
                    if bool(incomplete):
                        logging.info("Artifact Blocking Check: %s", focus)
                        self.deque_task()
                        self.queue_task(focus, *incomplete, silent=True)
                    elif bool(all_deps):
                        logging.debug("Artifact Unblocked: %s", focus)
                        self.update_state(focus, self.state_e.EXISTS)
                    else:
                        self.deque_task()
                        self.queue_task(focus)
                case self.state_e.WAIT | self.state_e.DEFINED: # Add dependencies of a task to the stack
                    incomplete, _ = self._task_dependencies(focus)
                    if bool(incomplete):
                        logging.info("Task Blocked: %s on : %s", focus, incomplete)
                        self.update_state(focus, self.state_e.WAIT)
                        self.deque_task()
                        self.queue_task(focus, *incomplete, silent=True)
                    else:
                        logging.debug("Task Unblocked: %s", focus)
                        self.update_state(focus, self.state_e.READY)

                case self.state_e.DECLARED: # warn on undefined tasks
                    logging.warning("Tried to Schedule a Declared but Undefined Task: %s", focus)
                    self.deque_task()
                    self.update_state(focus, self.state_e.SUCCESS)
                case _: # Error otherwise
                    raise doot.errors.DootTaskTrackingError("Unknown task state: ", x)

        return None
