from lib.counter import *

def test_counter_for_2():
    counter = Counter()
    counter.add(2)
    result = counter.report()
    assert result == "Counted to 2 so far."

def test_counter_for_4():
    counter = Counter()
    counter.add(4)
    result = counter.report()
    assert result == "Counted to 4 so far."