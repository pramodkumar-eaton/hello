import pytest

def func(x):
    return x + 1


def test_Question():
    assert func(3) == 5

def test_answer():
    assert func(4) == 5   


def test_answer():
    assert func(5) == 5      