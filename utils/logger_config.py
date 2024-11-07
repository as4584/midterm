import logging

class CalculatorLogger:
    def __init__(self, log_file_path='default_log.txt'):
        self.logger = logging.getLogger('CalculatorLogger')
        self.logger.setLevel(logging.DEBUG)
        handler = logging.FileHandler(log_file_path)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_user_action(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)

    def log_calculation(self, operation, num1, num2, result):
        self.logger.info(f"Calculation: {operation}({num1}, {num2}) = {result}") 