from utils.logger_config import CalculatorLogger

def test_log_user_action():
    logger = CalculatorLogger()
    action_message = "Performed addition: 3 + 5 = 8"
    logger.log_user_action(action_message)
    with open("logs/calculator.log") as log_file:
        log_contents = log_file.read()
    assert action_message in log_contents, "User action not logged correctly"

def test_log_error():
    logger = CalculatorLogger()
    error_message = "Division by zero error"
    logger.log_error(error_message)
    with open("logs/calculator.log") as log_file:
        log_contents = log_file.read()
    assert error_message in log_contents, "Error not logged correctly"
