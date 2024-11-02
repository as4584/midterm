from commands.command import Command

class AddCommand(Command):
    """Command that adds two numbers together."""
    
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b
    
    def execute(self) -> float:
        """Execute the add command.
        
        Returns:
            float: The sum of the two numbers.
        """
        return self.a + self.b
