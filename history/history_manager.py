import pandas as pd
from datetime import datetime

class CalculationHistory:
    def __init__(self):
        self.history_df = pd.DataFrame(columns=['timestamp', 'operation', 'num1', 'num2', 'result'])
    
    def add_calculation(self, operation, num1, num2, result):
        new_row = {
            'timestamp': datetime.now(),
            'operation': operation,
            'num1': num1,
            'num2': num2,
            'result': result
        }
        self.history_df = pd.concat([self.history_df, pd.DataFrame([new_row])], ignore_index=True)
    
    def view_history(self):
        if self.history_df.empty:
            print("No calculations in history.")
        else:
            print("\nCalculation History:")
            print(self.history_df.to_string(index=False))
    
    def clear_history(self):
        self.history_df = pd.DataFrame(columns=['timestamp', 'operation', 'num1', 'num2', 'result'])
        print("History cleared.") 