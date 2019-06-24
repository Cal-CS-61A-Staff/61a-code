import browser
import sys
import tb as traceback

_launchtext = """CS61A Python Web Interpreter
--------------------------------------------------------------------------------
Welcome to the 61A Python web interpreter! 
Check out the code for this app on GitHub.

To visualize a list, call draw(<list>).
To draw list visualizations automatically, call autodraw().
To view an environment diagram of your entire program, call visualize().
To launch an editor associated with your console, call editor().
"""

_credits = """    Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
    for supporting Python development.  See www.python.org for more information."""

_copyright = """Copyright (c) 2012, Pierre Quentel pierre.quentel@gmail.com
All Rights Reserved.

Copyright (c) 2001-2013 Python Software Foundation.
All Rights Reserved.

Copyright (c) 2000 BeOpen.com.
All Rights Reserved.

Copyright (c) 1995-2001 Corporation for National Research Initiatives.
All Rights Reserved.

Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
All Rights Reserved."""

_license = """Copyright (c) 2012, Pierre Quentel pierre.quentel@gmail.com
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer. Redistributions in binary
form must reproduce the above copyright notice, this list of conditions and
the following disclaimer in the documentation and/or other materials provided
with the distribution.
Neither the name of the <ORGANIZATION> nor the names of its contributors may
be used to endorse or promote products derived from this software without
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.
"""


class Stream:
    def __init__(self, obj):
        self.obj = obj

    def write(self, raw):
        self.obj.write(raw)


stdout = Stream(browser.self.stdout)
stderr = Stream(browser.self.stderr)


def credits():
    print(_credits)


credits.__repr__ = lambda: _credits


def copyright():
    print(_copyright)


copyright.__repr__ = lambda: _copyright


def license():
    print(_license)


license.__repr__ = lambda: _license


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

history = []
current = 0
_status = "main"  # or "block" if typing inside a block

autodraw_active = False


def json_repr(elem):
    if isinstance(elem, list):
        elem_reprs = [json_repr(x) for x in elem]
        return "[" + ", ".join(elem_reprs) + "]"
    elif isinstance(elem, str):
        return '"' + repr(elem)[1:-1] + '"'
    elif isinstance(elem, dict):
        key_val_reprs = [json_repr(key) + ": " + json_repr(val) for key, val in elem.items()]
        return "{" + ", ".join(key_val_reprs) + "}"
    elif isinstance(elem, bool):
        if elem:
            return "true"
        else:
            return "false"
    elif isinstance(elem, int):
        return '"' + repr(elem) + '"'
    else:
        raise Exception("Unable to serialize object of type " + str(type(elem)))


def wrap_debug(out):
    print("DRAW: " + json_repr(out))


def autodraw():
    global autodraw_active
    autodraw_active = True
    print("Call disable_autodraw() to disable automatic visualization of lists.")


def disable_autodraw():
    global autodraw_active
    autodraw_active = False
    print("Autodraw disabled.")


def atomic(elem):
    listlike = list, tuple
    return not isinstance(elem, listlike)


def inline(elem):
    inline = int, bool, float, str, type(None)
    return isinstance(elem, inline)


def draw(lst):
    heap = {}

    def draw_worker(elem):
        if inline(elem):
            return ["inline", repr(elem)]
        if atomic(elem):
            val = ["atomic", ["inline", repr(elem)]]
        elif len(elem) == 0:
            val = ["atomic", ["inline", "Empty list"]]
        else:
            val = ["list", [draw_worker(x) for x in elem]]
        heap[id(elem)] = val
        return ["ref", id(elem)]

    wrap_debug([draw_worker(lst), heap])


def visualize():
    print("DEBUG: ")


def editor():
    print("EDITOR: ")


def record_exec(code, wrap):
    if wrap:
        out = "try:\n"
        for line in code.split("\n"):
            out += "\t" + line + "\n"
        out += "except Exception as e:\n\tprint(e)\n"
        record_exec(out, False)
    else:
        print("EXEC: " + code)

# execution namespace
editor_ns = {'credits': credits,
             'copyright': copyright,
             'license': license,
             'autodraw': autodraw,
             'disable_autodraw': disable_autodraw,
             'draw': draw,
             'visualize': visualize,
             'editor': editor,
             '__name__': '__main__'}

first = True


def handleInput(line):
    global src, _status, first

    if first:
        if line.strip():
            try:
                exec(line, editor_ns)
                record_exec(line, False)
            except:
                record_exec(line, True)
                print_tb()
            write(">>> ")
        else:
            write(_launchtext)
            write("\n>>> ")
            # doc['code'].value += 'Type "copyright", "credits" or "license" for more information.'
        first = False
        return

    src += line[:-1]

    if _status == "main":
        current_line = src[src.rfind('>>>') + 4:]
    elif _status == "3string":
        current_line = src[src.rfind('>>>') + 4:]
        current_line = current_line.replace('\n... ', '\n')
    else:
        current_line = src[src.rfind('...') + 4:]

    src += "\n"

    if _status == 'main' and not current_line.strip():
        write('>>> ')
        return

    if _status == "main" or _status == "3string":
        try:
            _ = editor_ns['_'] = eval(current_line, editor_ns)
            record_exec(current_line, False)
            flush()
            if _ is not None:
                write(repr(_) + '\n')
                if not atomic(_) and autodraw_active:
                    draw(_)
            flush()
            write('>>> ')
            _status = "main"
        except IndentationError:
            write('... ')
            _status = "block"
        except SyntaxError as msg:
            if str(msg) == 'invalid syntax : triple string end not found' or \
                    str(msg).startswith('Unbalanced bracket'):
                write('... ')
                _status = "3string"
            elif str(msg) == 'eval() argument must be an expression':
                try:
                    exec(current_line, editor_ns)
                    record_exec(current_line, False)
                except:
                    print_tb()
                    record_exec(current_line, True)
                flush()
                write('>>> ')
                _status = "main"
            elif str(msg) == 'decorator expects function':
                write('... ')
                _status = "block"
            else:
                syntax_error(msg.args)
                write('>>> ')
                _status = "main"
        except:
            # the full traceback includes the call to eval(); to
            # remove it, it is stored in a buffer and the 2nd and 3rd
            # lines are removed
            record_exec(current_line, True)
            print_tb()
            write('>>> ')
            _status = "main"
    elif current_line == "":  # end of block
        block = src[src.rfind('>>>') + 4:].splitlines()
        block = [block[0]] + [b[4:] for b in block[1:]]
        block_src = '\n'.join(block)
        # status must be set before executing code in globals()
        _status = "main"
        try:
            _ = exec(block_src, editor_ns)
            record_exec(block_src, False)
            if _ is not None:
                print(repr(_))
        except:
            record_exec(block_src, True)
            print_tb()
        flush()
        write('>>> ')
    else:
        write('... ')


browser.self.stdin.on(handleInput)
