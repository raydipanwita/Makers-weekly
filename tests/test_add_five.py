from lib.add_five import *

def test_add_five_returns_eight_for_three():
    result = add_five(3)
    assert result == 8
def test_add_five_returns_fifteen_for_ten():
    result = add_five(10)
    assert result == 15