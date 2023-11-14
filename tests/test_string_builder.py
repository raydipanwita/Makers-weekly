from lib.string_builder import *
def test_stringbuilder_hello():
    word = StringBuilder()
    word.add("Hello")
    size = word.size
    assert word.size() == 5
    assert word.output() == "Hello"

def test_stringbuilder_morning():
    word = StringBuilder()
    word.add("Morning")
    size = word.size
    assert word.size() == 7
    assert word.output() == "Morning"

def test_stringbuilder_challenge():
    word = StringBuilder()
    word.add("Challenge")
    size = word.size
    assert word.size() == 9
    assert word.output() == "Challenge"