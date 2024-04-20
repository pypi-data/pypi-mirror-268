"""
@file   : color.py
@author : jiangmenggui@hosonsoft.com
@data   : 2024/4/2
"""
import re


class _Color:

    def __init__(self, s, start, end, name):
        self.raw = s
        self.s = start + s + end
        self.start = start
        self.end = end
        self.name = name

    def __len__(self):
        return self.raw.__len__()

    def __str__(self):
        return self.s.__str__()

    def __repr__(self):
        return self.s.__repr__()

    def __iter__(self):
        return self.raw.__iter__()

    def __add__(self, other):
        return self.s + other

    def __radd__(self, other):
        return other + self.s

    def __format__(self, format_spec):
        return self.start + self.raw.__format__(format_spec) + self.end


class _ColorFactory:

    def __init__(self, name, start, end='\033[0m'):
        self.name = name
        self.start = start
        self.end = end

    def __call__(self, s: str):
        return _Color(s, self.start, self.end, self.name)


class Color:
    UNDERLINE = '\033[4m'
    red = _ColorFactory('red', '\033[91m')
    green = _ColorFactory('green', '\033[92m')
    yellow = _ColorFactory('yellow', '\033[93m')
    blue = _ColorFactory('blue', '\033[94m')
    magenta = _ColorFactory('purple', '\033[95m')
    cyan = _ColorFactory('cyan', '\033[96m')
    white = _ColorFactory('white', '\033[97m')
    thin_red = _ColorFactory('red', '\033[31m')
    thin_green = _ColorFactory('green', '\033[32m')
    thin_yellow = _ColorFactory('yellow', '\033[33m')
    thin_blue = _ColorFactory('blue', '\033[34m')
    thin_magenta = _ColorFactory('purple', '\033[35m')
    thin_cyan = _ColorFactory('cyan', '\033[36m')
    thin_white = _ColorFactory('white', '\033[37m')

    success = green
    fail = red
    warning = yellow

    @classmethod
    def color(cls, val: str, style='i u r white on red'):
        colors = 'black red green yellow blue magenta cyan white'.split()
        style = re.split(r'\s+', style)
        values = set()
        for i in style:
            if i == 'i':
                values.add(3)
            elif i == 'u':
                values.add(4)
            elif i == 'r':
                values.add(7)
            elif i == 'on':
                next_color = style[style.index(i) + 1]
                values.add(colors.index(next_color) + 40)
            else:
                values.add(colors.index(i) + 30)

        return _ColorFactory('color', f'\033[{";".join(map(str, values))}m')(val)


if __name__ == '__main__':
    print(Color.red('hello world'))
    print(Color.green('hello world'))
    print(Color.yellow('hello world'))
    print(Color.blue('hello world'))
    print(Color.cyan('hello world'))
    print(Color.magenta('hello world'))
    print(Color.white('hello world'))
    print(Color.thin_red('hello world'))
    print(Color.thin_green('hello world'))
    print(Color.thin_yellow('hello world'))
    print(Color.thin_blue('hello world'))
    print(Color.thin_cyan('hello world'))
    print(Color.thin_magenta('hello world'))
    print(Color.thin_white('hello world'))
    print('ni hao ' + Color.red('world') + '!')
    print('|'.join(map(str, [Color.red('hello'), Color.green('world')])))
    print(Color.warning('warning: hello world'))
    print('\033[5;34;46mhello world\033[0m')
    print(Color.color('hello World', style='u black on yellow'))
    pass
