import pytest

from jar import Jar


def test_init_defaults():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    assert str(jar) == ""


def test_init_custom():
    jar = Jar(capacity=20)
    assert jar.capacity == 20
    assert jar.size == 0
    assert str(jar) == ""


def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪" * 3


def test_deposit_within_capacity():
    jar = Jar(capacity=5)
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(3)
    assert jar.size == 5


def test_deposit_over_capacity():
    jar = Jar(capacity=4)
    with pytest.raises(ValueError):
        jar.deposit(5)
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.deposit(3)


def test_withdraw_within_size():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2


def test_withdraw_too_many():
    jar = Jar()
    jar.deposit(2)
    with pytest.raises(ValueError):
        jar.withdraw(3)


def test_set_capacity_too_small():
    jar = Jar(capacity=5)
    with pytest.raises(ValueError):
        jar.deposit(6)


def test_set_capacity_negative():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.capacity = -1
