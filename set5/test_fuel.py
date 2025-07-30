import pytest

from fuel import convert, gauge


# Tests for convert
def test_convert_valid():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("0/1") == 0
    assert convert("1/1") == 100


def test_convert_rounding():
    assert convert("1/3") == 33
    assert convert("2/3") == 67


def test_convert_zero_denominator():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_convert_invalid_fraction():
    with pytest.raises(ValueError):
        convert("5/4")
        convert("-1/2")
        convert("1/-2")


def test_convert_non_integer():
    with pytest.raises(ValueError):
        convert("a/b")
        convert("1.5/2")


# Tests for gauge
def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_middle():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
