from flake8_no_nesting import Plugin
from typing import Set
from ast import parse
import pytest


def _results(s: str) -> Set[str]:
    tree = parse(s)
    plugin = Plugin(tree=tree)
    return {f'{line}:{col} {msg}' for line, col, msg, _ in plugin.run()}


def test_():
    assert _results('') == set()


@pytest.mark.parametrize('path,expected', [
    ('./tests/masters/if_in_for.py', {'3:8 FNN100 nested if found'}),
    ('./tests/masters/many_if_in_for.py', {
        '4:8 FNN100 nested if found',
        '6:8 FNN100 nested if found'
        }),
    ('./tests/masters/if_in_while.py', {'3:8 FNN100 nested if found'}),
    ('./tests/masters/if_in_if.py', {'3:8 FNN100 nested if found'}),
    ('./tests/masters/for_in_for.py', {'3:8 FNN101 nested for loop found'}),
    ('./tests/masters/for_in_if.py', {'3:8 FNN101 nested for loop found'}),
    ('./tests/masters/while_in_for.py', {'3:8 FNN102 nested while loop found'}),
    ('./tests/masters/while_in_if.py', {'3:8 FNN102 nested while loop found'}),
    ('./tests/masters/while_in_while.py', {'3:8 FNN102 nested while loop found'}),
    ('./tests/masters/for_in_while.py', {'3:8 FNN101 nested for loop found'}),
])
def test_fails_for_else(path, expected):
    with open(path, 'r') as file:
        func = file.read()
    ret = _results(func)
    assert ret == expected, type(ret)
