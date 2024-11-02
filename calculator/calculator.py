from utils.logger_config import CalculatorLogger
from history.history_manager import CalculationHistory
from plugins.plugin_loader import PluginLoader

def main():
    logger = CalculatorLogger()
    history = CalculationHistory()
    plugin_loader = PluginLoader(logger)
    
    # Load plugins
    plugins = plugin_loader.load_plugins()
    
    # Combine built-in operations with plugin operations
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else None
    }
    operations.update(plugins)
    
    logger.log_user_action("Calculator started")
    
    while True:
        try:
            # Get available operations including plugins
            available_ops = list(operations.keys()) + ['history', 'clear', 'help', 'exit']
            op_list = '/'.join(available_ops)
            
            user_input = input(f'[advanced calculator] What would you like to do? ({op_list}): ')
            logger.log_user_action(f"User selected: {user_input}")
            
            if user_input == 'exit':
                logger.log_user_action("Calculator ended")
                print("Goodbye!")
                break
                
            if user_input == 'history':
                history.view_history()
                continue
                
            if user_input == 'clear':
                history.clear_history()
                logger.log_user_action("History cleared")
                continue
                
            if user_input == 'help':
                print("\nAvailable operations:")
                for op in operations:
                    if op in plugins:
                        print(f"{op}: {plugin_loader.get_plugin_description(op)}")
                    else:
                        print(f"{op}: Basic arithmetic operation")
                continue
                
            if user_input in operations:
                num1 = int(input('enter first number: '))
                num2 = int(input('enter second number: '))
                
                try:
                    if user_input == 'divide' and num2 == 0:
                        error_msg = "Division by zero attempted"
                        logger.log_error(error_msg)
                        print("Error: Cannot divide by zero!")
                        continue
                    
                    if user_input in plugins:
                        result = plugin_loader.execute_plugin(user_input, num1, num2)
                    else:
                        result = operations[user_input](num1, num2)
                    
                    print(f"The answer is {result}")
                    history.add_calculation(user_input, num1, num2, result)
                    logger.log_calculation(user_input, num1, num2, result)
                    
                except Exception as e:
                    error_msg = f"Calculation error: {str(e)}"
                    logger.log_error(error_msg)
                    print(f"Error: {error_msg}")
            else:
                logger.log_error(f"Invalid input: {user_input}")
                print("Invalid input")
                
        except Exception as e:
            error_msg = f"General error: {str(e)}"
            logger.log_error(error_msg)
            print(f"An error occurred: {error_msg}")

if __name__ == "__main__":
    main() 