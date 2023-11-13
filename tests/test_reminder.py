from lib.reminder import *

def test_reminds_the_user_to_do_a_task_kay():
    reminder = Reminder("Kay")
    reminder.remind_me("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Kay!"

def test_reminds_the_user_to_do_a_task_kate():
    reminder = Reminder("Kate")
    reminder.remind_me("Go shopping")
    result = reminder.remind()
    assert result == "Go shopping, Kate!"