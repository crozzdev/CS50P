from datetime import date, timedelta

import pytest

from seasons import calculate_min_born, get_born_date


def test_get_born_date_valid():
    d = "2000-01-01"
    result = get_born_date(d)
    assert isinstance(result, date)
    assert result == date(2000, 1, 1)


def test_get_born_date_invalid_format():
    with pytest.raises(SystemExit):
        get_born_date("01-01-2000")


def test_get_born_date_future():
    future = (date.today() + timedelta(days=1)).isoformat()
    with pytest.raises(SystemExit):
        get_born_date(future)


def test_calculate_min_born_today():
    today = date.today()
    assert calculate_min_born(today) == 0


def test_calculate_min_born_past():
    days_ago = 10
    d = date.today() - timedelta(days=days_ago)
    assert calculate_min_born(d) == days_ago * 1440
