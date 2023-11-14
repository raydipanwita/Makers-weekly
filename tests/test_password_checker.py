import pytest
from lib.password_checker import *

"""
If password is 8 characters"""
def test_passwordchecker_8():
    password = PasswordChecker()
    assert password.check("12345678") == True

"""
If apssword is more than 8
"""
def test_passwordchecker_morethan8():
    password = PasswordChecker()
    assert password.check("123456789") == True
    
"""
If password is less than 8
"""
def test_passwordchecker_lessthan8():
    password = PasswordChecker()
    with pytest.raises (Exception) as e:
        password.check("1234567")
    error_message = str(e.value)
    assert error_message == "Invalid password, must be 8+ characters."
