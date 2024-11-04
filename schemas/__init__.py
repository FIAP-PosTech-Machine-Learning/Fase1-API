import os
import importlib

# Get the absolute path of the current directory (utils)
current_dir = os.path.dirname(__file__)

# Iterate over all files in the current directory
for filename in os.listdir(current_dir):
    # Check if the file ends with ".py" and is not __init__.py
    if filename.endswith(".py") and filename != "__init__.py":
        # Remove the .py extension to get the module name
        module_name = filename[:-3]
        # Dynamically import the module
        module = importlib.import_module(f'.{module_name}', package=__name__)
        
        # Get all public elements defined in the module and add them to the global namespace
        for attribute_name in dir(module):
            if not attribute_name.startswith("_"):
                globals()[attribute_name] = getattr(module, attribute_name)