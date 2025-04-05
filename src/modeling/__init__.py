from .data_processing import DataProcessor
from .model import ModelBuilder
from .utils import UtilityFunctions

# __init__.py

# This file marks the directory as a Python package and can be used to initialize the package.

# Importing modules or classes for easier access

# Defining the package version
__version__ = "1.0.0"

# Exposing key components at the package level
__all__ = ["DataProcessor", "ModelBuilder", "UtilityFunctions"]