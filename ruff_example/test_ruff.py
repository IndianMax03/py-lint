import os, sys

def test_ruff():
    x = lambda a : a + 10
    assert x != None, 'x is None'
    assert x(2) == 12, 'Invalid lambda!'
