from poetry_demo import Demo


def test_true():
    assert "DE" == "DE"


def test_hello_david():
    Demo.Demo.hello_world("david")


def test_hello_world():
    assert Demo.main() == "Hello World"


def test_hi_there():
    assert Demo.hi_there() == "Hi there"
