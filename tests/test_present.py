import pytest
from lib.present import *
"""
When we wrap an item
we get it back by unwrapping
"""

def test_present_wrap_and_unwrap():
    present = Present()
    present.wrap(3) 
    assert present.unwrap() == 3
    
"""
If we unwrap before wrapping
we get error message 
"""
def test_present_unwrap_without_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

"""
If we try to wrap an alreay wrapped present
we get an error message
"""
def test_already_wrapped_present():
    present = Present()
    present.wrap(40)
    with pytest.raises(Exception) as e:
        present.wrap(60)
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

"""
If we try to wrap already wrapped present
The first wrapped value is unchanged
"""
def test_already_wrapped_preserves_value():
    present = Present()
    present.wrap(40)
    with pytest.raises(Exception) as e:
        present.wrap(60)
    assert present.unwrap() == 40
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."


