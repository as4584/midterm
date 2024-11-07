import pytest
from calculator.calculator import Calculator
from history.history_manager import CalculationHistory
from plugins.plugin_loader import PluginLoader
from utils.logger_config import CalculatorLogger


def test_calculator_integration():
    """Test the calculator's main operations together with history and logging."""
    # Set up the necessary components
    logger = CalculatorLogger()
    history = CalculationHistory()
    plugin_loader = PluginLoader(logger)

    # Load plugins
    plugin_loader.load_plugins()
    
    # Perform basic operations using commands and verify history
    add_result = plugin_loader.execute_plugin("add", 3, 5)
    subtract_result = plugin_loader.execute_plugin("subtract", 10, 3)
    multiply_result = plugin_loader.execute_plugin("multiply", 4, 6)
    divide_result = plugin_loader.execute_plugin("divide", 8, 2)
    
    # Validate results
    assert add_result == 8, "Addition integration test failed"
    assert subtract_result == 7, "Subtraction integration test failed"
    assert multiply_result == 24, "Multiplication integration test failed"
    assert divide_result == 4, "Division integration test failed"

    # Add results to history and verify
    history.add_calculation("add", 3, 5, add_result)
    history.add_calculation("subtract", 10, 3, subtract_result)
    history.add_calculation("multiply", 4, 6, multiply_result)
    history.add_calculation("divide", 8, 2, divide_result)
    
    history_output = history.view_history()
    assert "add" in history_output, "Addition history integration failed"
    assert "subtract" in history_output, "Subtraction history integration failed"
    assert "multiply" in history_output, "Multiplication history integration failed"
    assert "divide" in history_output, "Division history integration failed"


def test_plugin_execution_with_history():
    """Test if plugins execute correctly and add to history."""
    # Set up components
    logger = CalculatorLogger()
    plugin_loader = PluginLoader(logger)
    history = CalculationHistory()
    
    # Load plugins
    plugin_loader.load_plugins()

    # Execute plugin and add to history
    result = plugin_loader.execute_plugin("sqrt", 16)
    assert result == 4, "Square root plugin execution failed"
    
    # Add to history
    history.add_calculation("sqrt", 16, None, result)
    history_output = history.view_history()
    assert "sqrt" in history_output, "Square root plugin not found in history"


def test_clear_history_after_operations():
    """Perform operations, clear history, and verify history is empty."""
    history = CalculationHistory()
    
    # Add some operations to history
    history.add_calculation("add", 3, 5, 8)
    history.add_calculation("subtract", 10, 3, 7)
    
    # Clear history
    history.clear_history()
    
    # Check if history is empty
    assert len(history.history_df) == 0, "History should be empty after clearing"
    assert history.view_history() == "", "History view should return an empty string after clearing"
