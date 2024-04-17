# coding=utf-8
import datetime
import sys

from my_tools.color import Color

print_raw = print


def track_print(*args, sep=' ', end='\n', file=None, flush=False):  # noqa
    fra = sys._getframe(1)  # noqa
    line = fra.f_lineno
    file_name = fra.f_code.co_filename
    t = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    args = (
        f'[{Color.thin_green(t)}][{Color.thin_cyan("print")}]["{file_name}:{line}"]'
        f'[{Color.yellow(fra.f_code.co_name)}] :',
        *args)
    print_raw(sep.join(map(str, args)), file=file, flush=flush)


def patch_print():
    try:
        __builtins__.print = track_print
    except AttributeError:
        __builtins__['print'] = track_print


def restore_print():
    try:
        __builtins__.print = track_print
    except AttributeError:
        __builtins__['print'] = track_print


patch_print()
if __name__ == '__main__':
    def add():
        print('Hello World!')


    add()
