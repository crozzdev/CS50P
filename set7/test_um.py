from um import count


def test_basic_ums():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1
    assert count("um?") == 1
    assert count("um, um.") == 2


def test_embedded_ums():
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umami") == 0


def test_multiple_ums():
    assert count("um um um") == 3
    assert count("Um, um, um!") == 3


def test_no_ums():
    assert count("hello world") == 0
