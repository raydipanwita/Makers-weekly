from lib.report_length import *

def test_report_length_1():
    assert report_length("H")

def test_report_length_12():
    assert report_length("hello") == "This string was 5 characters long."

def test_report_length_10():
    assert report_length("Good Morning") == "This string was 12 characters long."    

def test_report_length_27():
    assert report_length("Hi, my name is Harry Potter") == "This string was 27 characters long."
