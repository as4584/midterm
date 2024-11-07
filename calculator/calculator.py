# calculator/calculator.py
import os
import sys
from pathlib import Path
from dotenv import load_dotenv  # Import dotenv to load environment variables
from config import config_loader

# Load environment variables from .env file
load_dotenv()

# Add the project root directory to Python path
current_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(current_dir))

#importing my modules
from plugins.plugin_loader import PluginLoader
from utils.logger_config import CalculatorLogger
from history.history_manager import CalculationHistory
from commands.add_command import AddCommand
from commands.subtract_command import SubtractCommand
from commands.multiply_command import MultiplyCommand
from commands.divide_command import DivideCommand

log_file_path = Config.LOG_FILE_PATH
history_file_path = Config.HISTORY_FILE_PATH

def main():
    # Configure logger and history with environment variables
    log_file_path = os.getenv('LOG_FILE_PATH', 'default_log.txt')
    history_file_path = os.getenv('HISTORY_FILE_PATH', 'default_history.txt')
    
    logger = CalculatorLogger(log_file_path)
    history = CalculationHistory(history_file_path)
    plugin_loader = PluginLoader(logger)
    
    # Load plugins on startup
    plugins = plugin_loader.load_plugins()
    
    print("Welcome to Advanced Calculator!")
    print("Available commands: add, subtract, multiply, divide, history, clear, list_plugins, exit")
    
    while True:
        user_input = input("[advanced calculator] What operation would you like to do today? ").strip().lower()
        
        if user_input == "exit":
            logger.log_user_action("Calculator ended")
            print("Goodbye!")
            break
        elif user_input == "list_plugins":
            print("Available plugins:", plugin_loader.list_plugins())
            logger.log_user_action("Listed available plugins")
        elif user_input == "history":
            print(history.view_history())
            logger.log_user_action("History viewed")
        elif user_input == "clear":
            history.clear_history()
            logger.log_user_action("History cleared")
            print("History cleared.")
        elif user_input in ["add", "subtract", "multiply", "divide"]:
            # Prompt user for numbers and execute the corresponding command
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if user_input == "add":
                command = AddCommand(num1, num2)
            elif user_input == "subtract":
                command = SubtractCommand(num1, num2)
            elif user_input == "multiply":
                command = MultiplyCommand(num1, num2)
            elif user_input == "divide":
                command = DivideCommand(num1, num2)
            try:
                result = command.execute()
                print(f"The answer is {result}")
                history.add_calculation(user_input, num1, num2, result)
                logger.log_user_action(f"Executed {user_input} with {num1} and {num2} - Result: {result}")
            except Exception as e:
                print(f"Error: {e}")
                logger.log_error(f"Error executing {user_input}: {e}")
        elif user_input in plugins:
            # Execute plugin commands
            num1 = float(input("Enter a number: "))
            try:
                result = plugin_loader.execute_plugin(user_input, num1)
                print(f"The answer is {result}")
                history.add_calculation(user_input, num1, None, result)
                logger.log_user_action(f"Executed plugin {user_input} with {num1} - Result: {result}")
            except Exception as e:
                print(f"Error: {e}")
                logger.log_error(f"Error executing plugin {user_input}: {e}")
        else:
            print("Invalid input, please try again.")
            logger.log_error(f"Invalid input: {user_input}")

if __name__ == "__main__":
    main() 