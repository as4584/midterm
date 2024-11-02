from commands.command import Command

class SubtractCommand(Command):
    """Command that subtracts one number from another."""
    
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    def execute(self) -> float:
        """Execute the subtract command.
        
        Returns:
            float: The difference between the two numbers (a - b).
        """
        return self.a - self.b
