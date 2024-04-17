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

from random import random
import struct

logging = logmod.getLogger(__name__)

# BigEnd, continue?, msglen
head = struct.Struct(">?L")

kg =  b'keep going'
fin = b'finished'

served = 0

async def still_alive():
    while True:
        print("Still Alive")
        await asyncio.sleep(1)

async def handle_connection(reader, writer):
    message = None
    addr    = writer.get_extra_info('peername')
    print("Connection Opened: ", addr)

    count = 0
    while True:
        data    = await reader.read(head.size)
        match head.unpack(data):
            case True, size:
                count += 1
                print("Reading: ", size)
                data    = await reader.read(size)
                print("Message: ", data.decode())

                if count > 3:
                    response = head.pack(False, len(fin))
                    writer.write(response)
                    writer.write(kg)
                else:
                    response = head.pack(True, len(kg))
                    writer.write(response)
                    writer.write(kg)
                await writer.drain()
            case False, 0:
                break
            case _:
                raise Exception("Bad message received")

    print("Close the connection")
    writer.close()
    global served
    served += 1

async def main():
    server = await asyncio.start_server(handle_connection, '127.0.0.1', 8888)
    addr   = server.sockets[0].getsockname()
    print(f'Serving on {addr}')

    sa_task = asyncio.create_task(still_alive())
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())
