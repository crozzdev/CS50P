from bank import value


def test_hello_variants():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO there") == 0
    assert value("hello, friend") == 0


def test_h_only():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("Hmmm") == 20


def test_not_h():
    assert value("good morning") == 100
    assert value("what's up") == 100
    assert value("greetings") == 100
