import ast
import json
import os
import sys
from contextlib import redirect_stdout
from typing import Optional, TYPE_CHECKING
from io import StringIO

if TYPE_CHECKING:
    from scheme import *

WARN = True


def warn(*args):
    if WARN:
        print(*args, file=sys.stderr)


UNEVALUATED = "UNEVALUATED"
EVALUATING = "EVALUATING"
APPLYING = "APPLYING"
EVALUATED = "EVALUATED"


class DebuggingRun:
    def __init__(self):
        self.time = 0
        self.i = 0
        self.stack = []

        self.roots = DebugProp(self, None)

    def step(self):
        self.time += 1

    def id(self):
        self.i += 1
        return self.i

    def enter(self, node: 'DebugNode'):
        self.stack.append(node)

    def exit(self):
        self.stack.pop()

    def parent(self) -> Optional['DebugNode']:
        return self.stack[-1] if self.stack else None

    def add_root(self, root: 'DebugNode'):
        self.roots.update(root)

    def export(self):
        return json.dumps({
            "roots": self.roots.export(),
            "endTime": self.time,
        })


def scm_to_py_list(expr):
    out = []
    while isinstance(expr, Pair):
        out.append(expr.first)
        expr = expr.second
    return out


def make_debugger():
    run = DebuggingRun()
    cnt = 0

    def debug(scheme_eval):
        def decorated_scheme_eval(expr, env, tail=None):
            nonlocal cnt
            cnt += 1
            if cnt > 5000:
                raise SchemeError("Debugging is taking too long!")

            run.step()

            if run.parent() is None:
                node = DebugNode(expr, run)
                run.add_root(node)
            else:
                for child in run.parent().children.latest():
                    if expr is child.expr:
                        node = child
                        break
                else:
                    node = DebugNode(expr, run)
                    node.parent_str.update(run.parent().display_str.latest())
                    run.parent().state.update(APPLYING)
                    run.parent().children.update([node])

            if isinstance(expr, Pair):
                expr: DebugPair = impersonate(expr)
                children = []
                for sub_expr in scm_to_py_list(expr):
                    children.append(DebugNode(sub_expr, run))
                node.children.update(children)

            node.state.update(EVALUATING)

            run.enter(node)
            evaluated = scheme_eval(expr, env, tail)
            run.exit()

            run.step()

            node.state.update(EVALUATED)
            node.display_str.update(repl_str(evaluated))
            node.children.update([])

            return evaluated

        return decorated_scheme_eval

    return debug, run


class DebugNode:
    def __init__(self, expr, run: DebuggingRun):
        self.id = run.id()
        self.run = run
        self.expr = expr

        self.parent_str = DebugProp(run, repl_str(expr))
        self.display_str = DebugProp(run, repl_str(expr))
        self.state = DebugProp(run, UNEVALUATED)
        self.children = DebugProp(run, [])

    def export(self):
        return {
            "transitions": self.state.export(),
            "parent_strs": self.parent_str.export(),
            "strs": self.display_str.export(),
            "children": self.children.export(),
        }

    def __repr__(self):
        return f"DebugNode(" \
            f"expr={repr(self.expr)}, " \
            f"parent_str={repr(self.parent_str)}, " \
            f"display_str={repr(self.display_str)}, " \
            f"state={repr(self.state)}, " \
            f"children={repr(self.children)}, " \
            f"id={self.id}, " \
            f")"


class DebugProp:
    def __init__(self, run: DebuggingRun, start_val):
        self.run = run
        self.vals = [DebugVal(run.time, start_val)]

    def update(self, val):
        self.vals.append(DebugVal(self.run.time, val))

    def latest(self):
        return self.vals[-1].val

    def export(self):
        return [val.export() for val in self.vals]

    def __repr__(self):
        return f"DebugProp(vals={[val for val in self.vals if val.val is not None]})"


class DebugVal:
    def __init__(self, time: int, val):
        self.time = time
        self.val = val

    def export(self):
        if hasattr(self.val, "export"):
            return self.time, self.val.export()
        elif isinstance(self.val, list):
            return self.time, [val.export() for val in self.val]
        else:
            return self.time, self.val

    def __repr__(self):
        return f"DebugVal(time={self.time}, val={repr(self.val)})"


class DebugObj:
    id: int

    def __repr__(self):
        return f"DebugObj(obj={super().__repr__()}, fake_id={self.id}, real_id={id(self)})"


class DebugObjMutable(DebugObj):
    def __init__(self, *args, id):
        super().__init__(*args)
        self.id = id


class DebugObjImmutable(DebugObj):
    def __new__(cls, *args, id):
        obj = super().__new__(cls, *args)
        obj.id = id
        return obj


def get_id(obj):
    if isinstance(obj, DebugObj):
        return obj.id
    return id(obj)


def impersonate(obj) -> 'DebugObj':
    # if isinstance(obj, bool):
    #     return DebugBool(obj)
    # el

    if isinstance(obj, int):
        return DebugInt(obj, id=get_id(obj))
    elif isinstance(obj, Pair):
        return DebugPair(impersonate(obj.p94cc908), impersonate(obj.U__BH), id=get_id(obj))
    elif isinstance(obj, str):
        return DebugStr(obj, id=get_id(obj))
    elif isinstance(obj, nil.__class__):
        return DebugNil(id=get_id(obj))
    else:
        raise TypeError("Expected int, Pair, or str, received", obj, type(obj))


class DebugRewrite(ast.NodeTransformer):
    def visit_Compare(self, node):
        self.generic_visit(node)
        if len(node.ops) == 1 and isinstance(node.ops[0], ast.Is):
            return ast.fix_missing_locations(
                ast.Call(ast.Name("magic_is", ast.Load()), [node.left] + node.comparators, []))
        if len(node.ops) == 1 and isinstance(node.ops[0], ast.IsNot):
            return ast.fix_missing_locations(
                ast.UnaryOp(ast.Not(), ast.Call(ast.Name("magic_is", ast.Load()), [node.left] + node.comparators, [])))
        return node

    def visit_FunctionDef(self, node):
        if node.name == "debug":
            return None
        self.generic_visit(node)
        return node


def magic_is(a, b):
    return get_id(a) == get_id(b)


if __name__ == '__main__':
    target = os.path.join(os.path.dirname(os.path.abspath(__file__)), "interpreter.py")
    with open(target) as f:
        raw = f.read()
    tree = ast.parse(raw)
    DebugRewrite().visit(tree)

    debug, run = make_debugger()

    exec(compile(tree, filename="<scheme_debug>", mode="exec"))

    # class DebugBool(DebugObjImmutable, bool):
    #     ...


    class DebugInt(DebugObjImmutable, int):
        ...


    class DebugNil(DebugObjMutable, nil.__class__):
        def __eq__(self, other):
            return isinstance(other, nil.__class__)


    class DebugPair(DebugObjMutable, Pair):
        @property
        def first(self):
            return self.p94cc908

        @property
        def second(self):
            return self.U__BH

        ...


    class DebugStr(DebugObjImmutable, str):
        ...


    f = StringIO()

    with redirect_stdout(f):
       YY__LMP_(*sys.argv[1:]) # and this is y I love lamp

    print(run.export())
