# divide_command.py
import commands.command as command

from commands.command import Command

class DivideCommand(Command):
    """Command that divides one number by another."""
    
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    def execute(self) -> float:
        """Execute the divide command.
        
        Returns:
            float: The quotient of the two numbers (a / b).
            
        Raises:
            ValueError: If the divisor (b) is zero.
        """
        if self.b == 0:
            raise ValueError("Division by zero is not allowed")
        return self.a / self.b
