import pytest

from algorithm import StringCalulator

# Global
sc_obj = StringCalulator()


def test_sum_empty():
    assert 0 == sc_obj.sum()


def test_same_num():
    num = "3"
    assert 3 == sc_obj.sum(num)


def test_two_num():
    num = "1,2"
    assert 3 == sc_obj.sum(num)


def test_three_sum():
    num = "1,2,3"
    assert 6 == sc_obj.sum(num)


def test_new_line_sum():
    num = "1\n,2,3"
    assert 6 == sc_obj.sum(num)


def test_custom_delimiter_sum():
    num = "//;\n1;2"
    assert 3 == sc_obj.sum(num)


def test_single_negative_sum():
    num = "-5"
    assert "negatives not allowed: -5" == sc_obj.sum(num)


def test_multiple_negative_sum():
    num = "4,-5,6,-7"
    assert "negatives not allowed: -5 -7" == sc_obj.sum(num)


def test_single_thousands_sum():
    num = "1001"
    assert 0 == sc_obj.sum(num)


def test_multiple_thousands_sum():
    num = "2,1001"
    assert 2 == sc_obj.sum(num)
