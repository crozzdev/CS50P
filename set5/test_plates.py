from plates import is_valid


def test_valid_plates():
    assert is_valid("CS50") is True
    assert is_valid("AB123") is True
    assert is_valid("XY2345") is True
    assert is_valid("AB12") is True


def test_begins_with_two_letters():
    assert is_valid("A1234") is False
    assert is_valid("1BC23") is False
    assert is_valid("AB123") is True


def test_too_short_or_long():
    assert is_valid("A") is False
    assert is_valid("ABCDEFG") is False
    assert is_valid("") is False


def test_starts_with_non_letters():
    assert is_valid("1A23") is False
    assert is_valid("12AB") is False
    assert is_valid("3X") is False


def test_non_alphanumeric():
    assert is_valid("CS 50") is False
    assert is_valid("CS-50") is False
    assert is_valid("CS.50") is False


def test_number_placement():
    assert is_valid("CS05") is False  # leading zero in number
    assert is_valid("CS50A") is False  # letter after number
    assert is_valid("CS500") is True
    assert is_valid("CS5A0") is False


def test_no_numbers():
    assert is_valid("ABCDEF") is True


def test_only_one_zero():
    assert is_valid("AB0") is False  # leading zero
