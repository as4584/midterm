from commands.command import Command

class MultiplyCommand(Command):
    """Command that multiplies two numbers together."""
    
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    def execute(self) -> float:
        """Execute the multiply command.
        
        Returns:
            float: The product of the two numbers.
        """
        return self.a * self.b
