import pytest

from algorithm import add


def test_add_correct():
    assert 7 == add(4, 3)


def test_add_incorrect():
    assert 3 != add(4, 3)
