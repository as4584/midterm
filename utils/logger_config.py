import logging
from datetime import datetime
import os

class CalculatorLogger:
    def __init__(self):
        # Create logs directory if it doesn't exist
        if not os.path.exists('logs'):
            os.makedirs('logs')
            
        # Configure the logger
        self.logger = logging.getLogger('calculator')
        self.logger.setLevel(logging.DEBUG)
        
        # Create formatters
        file_formatter = logging.Formatter(
            '%(asctime)s | %(levelname)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_formatter = logging.Formatter('%(levelname)s: %(message)s')
        
        # File handler (logs everything)
        file_handler = logging.FileHandler(
            f'logs/calculator_{datetime.now().strftime("%Y%m%d")}.log'
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(file_formatter)
        
        # Console handler (logs warnings and errors)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.WARNING)
        console_handler.setFormatter(console_formatter)
        
        # Add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def log_calculation(self, operation, num1, num2, result):
        self.logger.info(
            f"Calculation performed: {num1} {operation} {num2} = {result}"
        )
    
    def log_error(self, error_message):
        self.logger.error(f"Error occurred: {error_message}")
    
    def log_user_action(self, action):
        self.logger.debug(f"User action: {action}") 