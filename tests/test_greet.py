from lib.greet import *
def test_greet_returns_dipa():
    result = greet("Dipa")
    assert result == ("Hello, Dipa!")

def test_greet_returns_jackjack():
    result = greet("JackJack")
    assert result == ("Hello, JackJack!")