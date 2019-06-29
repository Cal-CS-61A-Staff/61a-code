import browser
import sys
import tb as traceback

import static.scheme.scheme.IGNOREneeded as scheme

_launchtext = """CS61A Python Web Interpreter
--------------------------------------------------------------------------------
Welcome to the 61A Scheme web interpreter! 
Check out the code for this app on GitHub.

To visualize a list, call draw(<list>).
To draw list visualizations automatically, call autodraw().
To view an environment diagram of your entire program, call visualize().
To launch an editor associated with your console, call editor().
"""


class Stream:
    def __init__(self, obj):
        self.obj = obj

    def write(self, raw):
        self.obj.write(raw)


stdout = Stream(browser.self.stdout)
stderr = Stream(browser.self.stderr)


class Trace:
    def __init__(self):
        self.buf = ""

    def write(self, data):
        self.buf += str(data)

    def format(self):
        """Remove calls to function in this script from the traceback."""
        lines = self.buf.split("\n")
        stripped = [lines[0]]
        for i in range(1, len(lines), 2):
            if __file__ in lines[i]:
                continue
            stripped += lines[i: i + 2]
        return "\n".join(stripped)


def print_tb():
    trace = Trace()
    traceback.print_exc(file=trace)
    write(trace.format())


def syntax_error(args):
    info, filename, lineno, offset, line = args
    print(f"  File {filename}, line {lineno}")
    print("    " + line)
    print("    " + offset * " " + "^")
    print("SyntaxError:", info)
    flush()


OUT_BUFFER = ''
src = ""


def write(data):
    global OUT_BUFFER
    OUT_BUFFER += str(data)
    flush()


def flush():
    global OUT_BUFFER, src
    stdout.write(OUT_BUFFER)
    src += OUT_BUFFER
    OUT_BUFFER = ''


sys.stdout.write = sys.stderr.write = write
sys.stdout.__len__ = sys.stderr.__len__ = lambda: len(OUT_BUFFER)


def handleInput(line):
    write(dir(scheme))
    write("Indeed\nscm> ")


browser.self.stdin.on(handleInput)
