# invoker.py
# An invoker can manage and execute commands, making it easier to log operations or implement an undo feature if needed.

class Invoker:
    def __init__(self):
        self.history = []

    def execute_command(self, command):
        result = command.execute()
        self.history.append(command)
        return result
