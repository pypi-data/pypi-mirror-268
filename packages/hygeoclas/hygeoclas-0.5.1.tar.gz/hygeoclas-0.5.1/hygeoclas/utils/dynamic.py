import importlib

def import_class(importationPath: str, className: str):
    """Imports a class from a module.

    Args:
        importationPath (str): The import path of the module.
        className (str): The name of the class to import.

    Returns:
        classVariable: An instance of the imported class.

    Raises:
        ModuleNotFoundError: If the module is not found.
        AttributeError: If the class is not found in the module.
    """
    try:
        module = importlib.import_module(importationPath)
        classVariable = getattr(module, className)()
        return classVariable
    except ModuleNotFoundError:
        raise ModuleNotFoundError(f"Module {importationPath} was not found.") 
    except AttributeError:
        raise AttributeError(f"Class {className} was not found in module {className}.")