from history.history_manager import CalculationHistory

def test_add_to_history():
    history = CalculationHistory()
    history.add_calculation('add', 3, 5, 8)
    assert len(history.history_df) == 1, "Failed to add calculation to history"

def test_view_history():
    history = CalculationHistory()
    history.add_calculation('add', 3, 5, 8)
    history_output = history.view_history()
    assert "add" in history_output, "Failed to view history"

def test_clear_calculation_history():
    history = CalculationHistory()
    history.add_calculation('add', 3, 5, 8)
    history.add_calculation('subtract', 10, 3, 7)
    history.clear_history()
    assert len(history.history_df) == 0, "History should be empty after clearing"
    assert history.view_history() == "", "History view should return an empty string after clearing"

def test_calculation_history_multiple_entries():
    history = CalculationHistory()
    history.add_calculation('add', 3, 5, 8)
    history.add_calculation('subtract', 10, 3, 7)
    history.add_calculation('multiply', 4, 6, 24)
    history.add_calculation('divide', 8, 2, 4)
    history_output = history.view_history()
    assert "add" in history_output, "Addition calculation not found in history"
    assert "subtract" in history_output, "Subtraction calculation not found in history"
    assert "multiply" in history_output, "Multiplication calculation not found in history"
    assert "divide" in history_output, "Division calculation not found in history"
