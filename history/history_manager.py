import json
import os

class CalculationHistory:
    def __init__(self, history_file_path='default_history.txt'):
        self.history_file_path = history_file_path
        self.history = self.load_history()

    def load_history(self):
        if os.path.exists(self.history_file_path):
            with open(self.history_file_path, 'r') as file:
                return json.load(file)
        return []

    def add_calculation(self, operation, num1, num2, result):
        entry = {
            'operation': operation,
            'num1': num1,
            'num2': num2,
            'result': result
        }
        self.history.append(entry)
        self.save_history()

    def save_history(self):
        with open(self.history_file_path, 'w') as file:
            json.dump(self.history, file)

    def view_history(self):
        return self.history

    def clear_history(self):
        self.history = []
        self.save_history() 