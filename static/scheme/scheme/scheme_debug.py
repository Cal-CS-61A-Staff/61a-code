import ast
import json
import os
from contextlib import redirect_stdout
from typing import Optional, TYPE_CHECKING
from io import StringIO
from zipfile import ZipFile

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
                expr = impersonate(expr)
                assert isinstance(expr, DebugPair)
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
        return "DebugNode(" \
               "expr={expr}, " \
               "parent_str={parent_str}, " \
               "display_str={display_str}, " \
               "state={state}, " \
               "children={children}, " \
               "id={id}, " \
               ")".format(expr=repr(self.expr),
                          parent_str=repr(self.parent_str),
                          display_str=repr(self.display_str),
                          state=repr(self.state),
                          children=repr(self.children),
                          id=self.id)


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
        return "DebugProp(vals={vals})".format(vals=[val for val in self.vals if val.val is not None])


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
        return "DebugVal(time={time}, val={val})".format(time=self.time, val=repr(self.val))


class DebugObj:
    id = None

    def __repr__(self):
        return "DebugObj(obj={obj}, id={id})".format(obj=super().__repr__(), id=id(self))


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
        return DebugPair(impersonate(first(obj)), impersonate(second(obj)), id=get_id(obj))
    elif isinstance(obj, str):
        return DebugStr(obj, id=get_id(obj))
    elif isinstance(obj, nil.__class__):
        return DebugNil(id=get_id(obj))
    else:
        raise TypeError("Expected int, Pair, or str, received", obj, type(obj))


class NameDetector(ast.NodeVisitor):
    def __init__(self):
        self.names = {}

    def visit_Assign(self, node):
        targets, value = node.targets, node.value
        if isinstance(targets[0], ast.Name) and isinstance(value, ast.Name):
            target = targets[0].id
            self.names[target] = value.id

        self.generic_visit(node)


class DebugRewrite(ast.NodeTransformer):
    def __init__(self, lookup):
        self.lookup = lookup
        super()

    def visit_Compare(self, node):
        self.generic_visit(node)
        if len(node.ops) == 1 and isinstance(node.ops[0], ast.Is):
            return ast.fix_missing_locations(
                ast.Call(ast.Name("magic_is", ast.Load()), [node.left] + node.comparators, []))
        if len(node.ops) == 1 and isinstance(node.ops[0], ast.IsNot):
            return ast.fix_missing_locations(
                ast.UnaryOp(ast.Not(),
                            ast.Call(ast.Name("magic_is", ast.Load()), [node.left] + node.comparators, [])))
        return node

    def visit_FunctionDef(self, node):
        if node.name == "debug":
            return None
        elif node.name == self.lookup["scheme_eval"]:
            node.decorator_list.append(ast.fix_missing_locations(ast.Name("debug", ast.Load())))
        self.generic_visit(node)
        return node


# noinspection PyUnusedLocal
def magic_is(a, b):
    return get_id(a) == get_id(b)


def first(pair: 'Pair'):
    return pair.first


def second(pair: 'Pair'):
    return pair.second


zip_location = os.path.dirname(os.path.abspath(__file__))

with ZipFile(zip_location) as z:
    with z.open("scheme.py") as f:
        names_raw = f.read()
    with z.open("interpreter.py") as f:
        interpreter_raw = f.read()

detector = NameDetector()
detector.visit(ast.parse(names_raw))
lookup = detector.names

interpreter_tree = ast.parse(interpreter_raw)
DebugRewrite(lookup).visit(interpreter_tree)

debug, run = make_debugger()

exec(compile(interpreter_tree, filename="<scheme_debug>", mode="exec"))


class DebugInt(DebugObjImmutable, int):
    pass


class DebugNil(DebugObjMutable, nil.__class__):
    def __eq__(self, other):
        return isinstance(other, nil.__class__)


class DebugPair(DebugObjMutable, Pair):
    pass


class DebugStr(DebugObjImmutable, str):
    pass


def debug_run():
    f = StringIO()

    with redirect_stdout(f):
        eval(lookup["run"])(*sys.argv[1:])

    print(run.export())
