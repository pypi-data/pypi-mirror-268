# Import necessary modules/classes/functions for easy access when the library is imported
from .datamapper import map
from .common_utils import DEFAULT_VALUE, FILTER_VALUE

# List of names to be exported when using `from dataforgetoolkit import *`
__all__ = ['map', 'DEFAULT_VALUE', 'FILTER_VALUE',"REPLACE_VALUE","CONCAT_VALUE","UPPERCASE_VALUE","LOWERCASE_VALUE"]

# Author information
__author__ = "Amit Singh"

#Purpose of the library
__doc__ = """
DataForgeToolkit: A library for mapping CSV or Excel files based on JSON transformation mappings.

Usage:
    import dataforgetoolkit

    # Map a CSV or Excel file based on a JSON transformation mapping
    mapped_data = dataforgetoolkit.map(report_file_path, transformation_file_path)

    # Access common utilities
    default_value = dataforgetoolkit.DEFAULT_VALUE
    filter_value = dataforgetoolkit.FILTER_VALUE
"""
