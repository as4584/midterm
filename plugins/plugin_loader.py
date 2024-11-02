import os
import importlib
import inspect
from plugins.base_plugin import CalculatorPlugin

class PluginLoader:
    def __init__(self, logger):
        self.plugins = {}
        self.logger = logger
        
    def load_plugins(self):
        """Load all plugins from the plugins directory"""
        plugin_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Get all Python files in the plugins directory
        for filename in os.listdir(plugin_dir):
            if filename.endswith('.py') and filename not in ['__init__.py', 'plugin_loader.py', 'base_plugin.py']:
                try:
                    # Convert filename to module name
                    module_name = f"plugins.{filename[:-3]}"
                    
                    # Import the module
                    module = importlib.import_module(module_name)
                    
                    # Find all classes in the module that inherit from CalculatorPlugin
                    for name, obj in inspect.getmembers(module):
                        if (inspect.isclass(obj) and 
                            issubclass(obj, CalculatorPlugin) and 
                            obj != CalculatorPlugin):
                            
                            # Instantiate the plugin
                            plugin = obj()
                            plugin_name = plugin.get_name()
                            
                            # Register the plugin
                            self.plugins[plugin_name] = plugin
                            self.logger.log_user_action(f"Loaded plugin: {plugin_name}")
                            
                except Exception as e:
                    self.logger.log_error(f"Error loading plugin {filename}: {str(e)}")
        
        return self.plugins
    
    def get_available_operations(self):
        """Return a list of available plugin operations"""
        return list(self.plugins.keys())
    
    def get_plugin_description(self, plugin_name):
        """Return the description of a specific plugin"""
        if plugin_name in self.plugins:
            return self.plugins[plugin_name].get_description()
        return None
    
    def execute_plugin(self, plugin_name, num1, num2):
        """Execute a specific plugin operation"""
        if plugin_name in self.plugins:
            return self.plugins[plugin_name].execute(num1, num2)
        raise ValueError(f"Plugin {plugin_name} not found") 