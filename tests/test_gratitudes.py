from lib.gratitudes import *

def test_gratitudes_yourself():
    word = Gratitudes()
    word.add("Yourself")
    result = word.format()
    assert result == "Be grateful for: Yourself"

def test_gratitudes_family():
    word = Gratitudes()
    word.add("Family")
    result = word.format()
    assert result == "Be grateful for: Family"    
