"""
Commands for the REPL

"""
##-- imports
from __future__ import annotations

import importlib
import logging as logmod
import re
import traceback
from datetime import datetime
from enum import Enum
from os.path import abspath, exists, expanduser, split, splitext

##-- end imports

logging = logmod.getLogger(__name__)

import acab
import pyparsing as pp

try:
    import readline
except ImportError:
    readline = None

config  = acab.config

@register
def do_prompt(self, line):
    """
    Change the prompt of the repl

    Usage:
    prompt {newprompt}
    """
    self.state.prompt = line.strip()

@register
def do_multi(self, line):
    """
    Activate multi-line collation

    """
    if not self.state.in_multi_line:
        # Start
        logging.info("Activating multi line")
        self.state.in_multi_line = True
        self.state.collect_str = []
        self.state.prompt_bkup = self.state.prompt
        self.state.prompt = self.state.prompt_ml
        self.state.indent = 0
        if bool(readline):
            # indent modification based on:
            # https://stackoverflow.com/questions/8505163
            def input_hook():
                indent_str = self.state.indent * "    "
                readline.insert_text(indent_str)
                readline.redisplay()

            readline.set_pre_input_hook(input_hook)
    else:
        logging.info("Deactivating multi line")
        collected = "\n".join(self.state.collect_str)
        self.state.in_multi_line = False
        self.state.prompt = self.state.prompt_bkup
        self.state.indent = 0
        if bool(readline):
            readline.set_pre_input_hook()

        logging.info(f"Collected: {collected}")
        if bool(line):
            self.onecmd(line + " " + collected)
        else:
            self.onecmd(collected)




@register
def do_pop(self, line):
    """
    Pop off the last string added in multi-line mode,
    for when an error was made
    """
    self.state.collect_str.pop()
    logging.info(f"Collecting: {self.state.collect_str}")

@register
def do_collect(self, line):
    """ Add a line to the multi line collection,
    ready to be used as one statement when multi line is closed """
    assert(self.state.in_multi_line)
    if line.strip() == "end":
        self.state.indent = max(self.state.indent - 1, 0)


    curr_indent = self.state.indent
    curr_indent_str = curr_indent * "    "

    self.state.collect_str.append(curr_indent_str + line)
    if line[-1] == ":":
        self.state.indent += 1

    logging.info("Collecting: {}".format(self.state.collect_str))

@register
def do_echo(self, line):
    """
    Toggle echoing of working memory state
    """
    self.state.echo = not self.state.echo


@register
def do_suppress(self, line):
    """
    Repl Command to suppress all repl commands
    (except itself and `exit`.)
    """
    # TODO
    return
