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

import asyncio
import struct

# BigEnd, continue?, msglen
head = struct.Struct(">?L")

async def tcp_echo_client(message):
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)

    print(f'Sent: {message!r}')
    b_message = message.encode()
    writer.write(head.pack(True, len(b_message)))
    writer.write(b_message)
    await writer.drain()

    while True:
        data = await reader.read(head.size)
        match head.unpack(data):
            case True, size:
                print("Reading: ", size)
                data  = await reader.read(size)
                print("Message: ", data.decode())
                writer.write(head.pack(True, len(b_message)))
                writer.write(b_message)
                await writer.drain()
                await asyncio.sleep(1)
            case False, size:
                response = head.pack(False, 0)
                writer.write(response)
                await writer.drain()
                break
            case _:
                raise Exception("Bad Message Received")

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

asyncio.run(tcp_echo_client('Hello World!'))
