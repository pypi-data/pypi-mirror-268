from ast import AST, NodeVisitor, FunctionDef, ClassDef, Module
from typing import Generator, Any, Tuple, Type

import importlib.metadata as importlib_metadata


class Visitor(NodeVisitor):
    def __init__(self, f_ln, c_ln, m_ln):
        self.errors = []
        self.f_ln = f_ln
        self.c_ln = c_ln
        self.m_ln = m_ln

    def get_start_lineno(self, node):
        if isinstance(node, Module):
            return 1
        return node.lineno

    def get_start_colno(self, node):
        if isinstance(node, Module):
            return 0
        return node.col_offset

    def find_errors(self, node, err_msg, max_lines):
        lines_without_def = self.count_lines(node) - 1
        if not isinstance(node, Module):
            o_name = node.name
        if isinstance(node, Module):
            o_name = 'File'
        if lines_without_def > max_lines:
            self.errors.append((
                self.get_start_lineno(node),
                self.get_start_colno(node),
                err_msg.format(
                    o_name=o_name,
                    lines_without_def=lines_without_def,
                    max_lines=max_lines)))

    def count_lines(self, node: AST) -> int:
        count = 1
        if not hasattr(node, 'body'):
            return count
        if not isinstance(node.body, list):
            return count + self.count_lines(node.body)
        for n in node.body:
            count += self.count_lines(n)
        return count

    def visit_FunctionDef(self, node: FunctionDef) -> Any:
        err_msg = 'FSE100 Function {o_name} has too many lines ({lines_without_def} > {max_lines})'
        self.find_errors(node, err_msg, max_lines=self.f_ln)
        self.generic_visit(node)

    def visit_ClassDef(self, node: ClassDef) -> Any:
        err_msg = 'FSE101 Class {o_name} has too many lines ({lines_without_def} > {max_lines})'
        self.find_errors(node, err_msg, max_lines=self.c_ln)
        self.generic_visit(node)

    def visit_Module(self, node: Module) -> Any:
        err_msg = 'FSE102 {o_name} has too many lines ({lines_without_def} > {max_lines})'
        self.find_errors(node, err_msg, max_lines=self.m_ln)
        self.generic_visit(node)


class Plugin:
    name = __name__
    version = importlib_metadata.version(__name__)

    def __init__(self, tree: AST):
        self.tree = tree

    @classmethod
    def add_options(cls, parser) -> None:
        parser.add_option(
            "--max-fn-lines", type=int, default=15,
            help="Maximum number of lines in a function")
        parser.add_option(
            "--max-class-lines", type=int, default=50,
            help="Maximum number of lines in a class")
        parser.add_option(
            "--max-module-lines", type=int, default=200,
            help="Maximum number of lines in a module")

    @classmethod
    def parse_options(cls, options):
        cls.max_fn_lines = options.max_fn_lines
        cls.max_class_lines = options.max_class_lines
        cls.max_module_lines = options.max_module_lines

    def run(self) -> Generator[Tuple[int, int, str, Type[Any]], None, None]:
        visitor = Visitor(self.max_fn_lines, self.max_class_lines, self.max_module_lines)
        visitor.visit(self.tree)

        for error in visitor.errors:
            yield error + (type(self),)
