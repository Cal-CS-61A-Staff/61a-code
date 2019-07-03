# noinspection PyUnreachableCode

import browser

if False:
    from IGNORE_needed import *

# brython nonsense!
_launchtext = """CS61A Scheme Web Interpreter
--------------------------------------------------------------------------------
Welcome to the 61A Scheme web interpreter! 
Source for this interpreter is restricted.

[in the future] To visualize a list, call (draw <list>).
[in the future] To draw list visualizations automatically, call (autodraw).
[in the future] To view an environment diagram of your entire program, call (visualize).
To launch an editor associated with your console, call (editor).
"""


class Stream:
    def __init__(self, obj):
        self.obj = obj

    def write(self, raw):
        self.obj.write(raw)


def write(data):
    stdout.write(str(data))


sys.stdout.write = sys.stderr.write = write
sys.stdout.__len__ = sys.stderr.__len__ = lambda: 0

stdout = Stream(browser.self.stdout)
stderr = Stream(browser.self.stderr)

src = ""
firstLine = True


@builtin("editor")
def editor():
    print("EDITOR: ")


frame = create_global_frame()

DEBUG_HOOK = "DEBUG: "

def handle_input(line):
    global src, firstLine
    if firstLine:
        debugging = line.startswith(DEBUG_HOOK)
        if debugging:
            line = line[len(DEBUG_HOOK):]
        callback = (lambda x: debug_eval(x, frame)) if debugging else run_expr
        firstLine = False
        if not line:
            print(_launchtext)
        try:
            buff = Buffer(tokenize_lines(line.split("\n")))
            while buff.current():
                callback(scheme_read(buff))
        except Exception as err:
            print("ParseError:", err)
        write("scm> ")
    else:
        src += line
        try:
            buff = Buffer(tokenize_lines(src.split("\n")))
            while buff.more_on_line:
                run_expr(scheme_read(buff))
        except Exception as err:
            if isinstance(err, EOFError) or "unexpected end" in repr(err):
                write("...> ")
                return
            print("ParseError:", err)
        src = ""
        write("scm> ")


def run_expr(expr):
    try:
        ret = scheme_eval(expr, frame)
        if ret is not None:
            print(ret)
    except Exception as err:
        handle_error(frame)
        if isinstance(err, RuntimeError):
            print('Error: maximum recursion depth exceeded')
        else:
            print('Error:', err)


browser.self.stdin.on(handle_input)
