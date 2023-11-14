import pytest
from lib.reminder import *

def test_reminds_the_user_to_do_a_task_kay():
    reminder = Reminder("Kay")
    with pytest.raises(Exception)as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No reminder set!"

def test_reminds_the_user_to_do_a_task_kate():
    reminder = Reminder("Kate")
    reminder.remind_me("Go shopping")
    result = reminder.remind()
    assert result == "Go shopping, Kate!"