from lib.check_codeword import *

def test_check_codeword_hello_hose_horse():
    #
    assert check_codeword("horse") == "Correct! Come in."
    assert check_codeword("hose") == "Close, but nope."
    assert check_codeword("hello") == "Wrong"

def test_check_codeword_hose_goodbye():
    assert check_codeword("hoe") == "Close, but nope."
    assert check_codeword("goodbye") == "Wrong"
