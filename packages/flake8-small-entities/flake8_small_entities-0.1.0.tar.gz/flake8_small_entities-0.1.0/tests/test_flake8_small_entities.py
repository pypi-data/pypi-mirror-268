from flake8_small_entities import Plugin
from typing import Set
from ast import parse
import pytest


def _results(s: str) -> Set[str]:
    tree = parse(s)

    Plugin.max_fn_lines = 15
    Plugin.max_class_lines = 15
    Plugin.max_module_lines = 40

    plugin = Plugin(tree=tree)
    return {f'{line}:{col} {msg}' for line, col, msg, _ in plugin.run()}


def test_():
    assert _results('') == set()


@pytest.mark.parametrize('path, expected', ([
    [
        './tests/masters/long_function_code_only.py',
        {'1:0 FSE100 Function tstme has too many lines (16 > 15)'}],
    [
        './tests/masters/long_function_with_empty_lines.py',
        {'1:0 FSE100 Function tstme has too many lines (16 > 15)'}],
    [
        './tests/masters/long_function_with_comments.py',
        {'1:0 FSE100 Function tstme has too many lines (16 > 15)'}],
    [
        './tests/masters/long_function_with_nesting.py',
        {'1:0 FSE100 Function tstme has too many lines (20 > 15)'}],
    [
        './tests/masters/long_class.py',
        {'1:0 FSE101 Class tstme has too many lines (18 > 15)'}],
    [
        './tests/masters/long_file.py',
        {'1:0 FSE102 File has too many lines (45 > 40)'}],

]))
def test_para(path, expected):
    with open(path, 'r') as file:
        func = file.read()
    ret = _results(func)
    assert ret == expected, f'{path}, {ret}'
