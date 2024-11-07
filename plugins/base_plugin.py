class CalculatorPlugin:
    """Base class for all calculator plugins."""

    def get_name(self):
        """Return the name of the plugin."""
        raise NotImplementedError("This method must be overridden by the plugin.")

    def get_description(self):
        """Return a description of the plugin."""
        raise NotImplementedError("This method must be overridden by the plugin.")

    def execute(self, num1, num2):
        """Execute the plugin's operation with the given numbers."""
        raise NotImplementedError("This method must be overridden by the plugin.") 