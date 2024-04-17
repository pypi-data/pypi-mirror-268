#!/usr/bin/env python3

"""Run a command and complain only after a while
"""

import curses
import os
import signal
import sys
from asyncio import Queue, StreamReader
from asyncio import TimeoutError as AsyncTimeoutError
from asyncio import create_subprocess_exec, gather, run, wait_for
from asyncio.subprocess import PIPE, Process
from collections.abc import Sequence
from contextlib import suppress
from typing import TextIO

LineQueue = Queue[None | tuple[TextIO, bytes]]


async def print_after(
    timeout: float,
    abort: Queue[bool],
    buffer: LineQueue,
) -> None:
    """Wait for a given time or until aborted - print buffer contents if appropriate"""
    with suppress(AsyncTimeoutError):
        if await wait_for(abort.get(), timeout):
            return
    while elem := await buffer.get():
        out_file, line = elem
        out_file.write(line.decode(errors="replace"))


async def buffer_stream(stream: StreamReader, buffer: LineQueue, out_file: TextIO) -> None:
    """Records a given stream to a buffer line by line along with the source"""
    while line := await stream.readline():
        await buffer.put((out_file, line))
    await buffer.put(None)


async def wait_and_notify(process: Process, abort: Queue[bool]) -> None:
    """Just waits for @process to finish and notify the result"""
    await process.wait()
    await abort.put(process.returncode == 0)


async def run_quiet_and_verbose(timeout: float, cmd: Sequence[str]) -> int:
    """Run a command and start printing it's output only after a given timeout"""
    buffer: LineQueue = Queue()
    abort: Queue[bool] = Queue()

    process = await create_subprocess_exec(*cmd, stdout=PIPE, stderr=PIPE)

    assert process.stdout
    assert process.stderr

    signal.signal(signal.SIGINT, lambda _sig, _frame: 0)

    await gather(
        print_after(float(timeout), abort, buffer),
        buffer_stream(process.stdout, buffer, sys.stdout),
        buffer_stream(process.stderr, buffer, sys.stderr),
        wait_and_notify(process, abort),
    )
    return process.returncode


def main() -> None:
    """Just the entrypoint for run_quiet_and_verbose()"""
    timeout, *cmd = sys.argv[1:]
    curses.endwin()
    stdscr = curses.initscr()
    try:
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(1)
        try:
            curses.start_color()
        except:
            pass

        x = run(run_quiet_and_verbose(float(timeout), cmd))
    finally:
        stdscr.keypad(0)
        curses.echo()
        curses.nocbreak()
        #curses.endwin()
        curses.resetty()
    print(x)

if __name__ == "__main__":
    main()

"""
#!/usr/bin/env python3
def wrap(func, /, *args, **kwds):
    try:
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(1)
        try:
            curses.start_color()
        except:
            pass

        return func(stdscr, *args, **kwds)
    finally:
        if 'stdscr' in locals():
            stdscr.keypad(0)
            curses.echo()
            curses.nocbreak()
            curses.endwin()

def main(stdscr):
    print("Hallo")
    os.system(" ".join(sys.argv[1:]))
    ## Your script's output goes here
    #stdscr.addstr("Hello, I will be cleared in 2 seconds.")
    #stdscr.refresh()
    #curses.napms(2000) # Wait for 2 seconds

    # Clear the screen buffer and set the cursor to 0,0
    #stdscr.clear()
    #stdscr.refresh()
    #curses.napms(2000) # Wait for 2 seconds

if __name__ == "__main__":
    wrap(main)

"""
