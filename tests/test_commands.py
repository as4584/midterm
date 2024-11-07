import pytest
from commands.add_command import AddCommand
from commands.subtract_command import SubtractCommand
from commands.multiply_command import MultiplyCommand
from commands.divide_command import DivideCommand

def test_addition():
    add_command = AddCommand(3, 5)
    assert add_command.execute() == 8, "Addition failed"

def test_subtraction():
    subtract_command = SubtractCommand(10, 3)
    assert subtract_command.execute() == 7, "Subtraction failed"

def test_multiplication():
    multiply_command = MultiplyCommand(4, 6)
    assert multiply_command.execute() == 24, "Multiplication failed"

def test_division():
    divide_command = DivideCommand(8, 2)
    assert divide_command.execute() == 4, "Division failed"

def test_division_by_zero():
    with pytest.raises(ValueError, match="Division by zero is not allowed"):
        divide_command = DivideCommand(5, 0)
        divide_command.execute()
