from numb3rs import validate


def test_valid_ips():
    assert validate("0.0.0.0") is True
    assert validate("255.255.255.255") is True
    assert validate("192.168.1.1") is True
    assert validate("127.0.0.1") is True
    assert validate("10.0.0.1") is True
    assert validate("1.2.3.4") is True
    assert validate("99.99.99.99") is True


def test_invalid_ips():
    assert validate("256.100.100.100") is False
    assert validate("192.168.1.256") is False
    assert validate("300.0.0.1") is False
    assert validate("192.168.1") is False
    assert validate("192.168.1.1.1") is False
    assert validate("abc.def.ghi.jkl") is False
    assert validate("123.456.78.90") is False
    assert validate("1.2.3.04") is False  # leading zero
    assert validate("") is False
