from abc import ABC, abstractmethod

class Command(ABC):
    """Base interface for all command objects."""
    
    @abstractmethod
    def execute(self) -> None:
        """Execute the command's action.
        
        All derived command classes must implement this method.
        """
        pass
