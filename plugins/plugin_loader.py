import os
import importlib
from utils.logger_config import CalculatorLogger
from .base_plugin import CalculatorPlugin

class PluginLoader:
    """Class to load and manage calculator plugins."""

    def __init__(self, logger: CalculatorLogger):
        self.logger = logger
        self.plugins = {}

        self.load_plugins()

    def load_plugins(self):
        """Dynamically load plugins from the plugins directory."""
        plugins_dir = os.path.dirname(__file__)
        for filename in os.listdir(plugins_dir):
            if filename.endswith('.py') and filename not in ['base_plugin.py', 'plugin_loader.py']:
                module_name = filename[:-3]  # Remove .py extension
                module = importlib.import_module(f'.{module_name}', package='plugins')
                
                # Register all classes that inherit from CalculatorPlugin
                for attr in dir(module):
                    cls = getattr(module, attr)
                    if isinstance(cls, type) and issubclass(cls, CalculatorPlugin) and cls is not CalculatorPlugin:
                        plugin_instance = cls()
                        self.plugins[plugin_instance.get_name()] = plugin_instance
                        self.logger.log(f"Loaded plugin: {plugin_instance.get_name()}")

    def list_plugins(self):
        """Return a list of available plugin names."""
        return list(self.plugins.keys())

    def execute_plugin(self, command_name, num1, num2):
        """Execute a plugin's command with the given numbers."""
        if command_name in self.plugins:
            return self.plugins[command_name].execute(num1, num2)
        else:
            raise ValueError(f"Plugin '{command_name}' not found.")
        
        