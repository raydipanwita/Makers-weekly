class Reminder():
    def __init__(self, name):
        self.name = name
        self.task = None

    def remind_me(self, task):
        self.task = task

    def remind(self):
        if self.task is None:                 # We want to fail if there is no reminder yet.
            raise Exception("No reminder set!")
        return f"{self.task}, {self.name}!"