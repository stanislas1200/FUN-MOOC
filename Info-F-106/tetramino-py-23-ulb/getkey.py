"""Reads key press using a blocking call.

This module allows the user to read key presses immediately,
as the keys are typed, without having to press the Enter key.

When executed directly from the command line, this script displays the
bytes representing a key press, followed by a developer-friendly name
of the key.
"""

import os
import sys
import termios
import tty
from typing import Tuple


def getkey() -> Tuple[bytes, str]:
    """Read key press. This is a blocking function."""
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setcbreak(fd) # https://en.wikipedia.org/wiki/Terminal_mode
    try:
        b = os.read(fd, 5) # read up to 5 bytes

        key_mapping = {
            (127,): 'backspace',
            (10,): 'return',
            (32,): 'space',
            (9,): 'tab',
            (27,): 'esc',
            (27, 91, 65): 'up',
            (27, 91, 66,): 'down',
            (27, 91, 67,): 'right',
            (27, 91, 68,): 'left',
            (27, 91, 72): 'home',
            (27, 91, 70): 'end',
            (27, 91, 50, 126): 'insert',
            (27, 91, 51, 126): 'delete',
            (27, 91, 53, 126): 'pageup',
            (27, 91, 54, 126): 'pagedown',
            (27, 79, 80): 'f1',
            (27, 79, 81): 'f2',
            (27, 79, 82): 'f3',
            (27, 79, 83): 'f4',
            (27, 91, 49, 53, 126): 'f5',
            (27, 91, 49, 55, 126): 'f6',
            (27, 91, 49, 56, 126): 'f7',
            (27, 91, 49, 57, 126): 'f8',
            (27, 91, 50, 48, 126): 'f9',
            (27, 91, 50, 49, 126): 'f10',
            # F11 is already used to toggle fullscreen.
            (27, 91, 50, 52, 126): 'f12',
        }

        keyname = key_mapping.get(tuple(b), 'unknown')
        if keyname == 'unknown' and len(b) == 1:
            # Check for printable ASCII characters 33-126.
            n = ord(b)
            if n >= 33 and n <= 126:
                keyname = chr(n)
        return b, keyname
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


if __name__ == '__main__':
    print('Press ESCAPE or CTRL-C to quit.')
    try:
        while True:
            b, keyname = getkey()
            print(f'{b}, {tuple(b)}, len={len(b)}, keyname={keyname}')
            if keyname == 'esc':
                sys.exit()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        os.system('stty sane')
        print('bye.')
