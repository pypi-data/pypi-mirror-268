"""
    ___      __  __             __________  _  __
   / _ )___ / /_/ /____ ______ / / __/ __ \/ |/ /
  / _  / -_) __/ __/ -_) __/ // /\ \/ /_/ /    / 
 /____/\__/\__/\__/\__/_/  \___/___/\____/_/|_/  

BetterJSON is a Python library that provides a simple 
interface for working with JSON data. It includes functions 
for loading JSON data from a file, formatting a Python 
dictionary as a JSON string, and writing JSON data to a file.

Author: 
>> ruxixa

Version: 
>> 0.0.1

License:
>> MIT

Project URL:
>> https://github.com/ruxixa/BetterJSON
"""

from .modules.format import format_json
from .modules.parse import parse_json
from .__version__ import __version__

import os

def load(file_path: str) -> dict:
    """
    Parses a JSON file into a Python dictionary.

    Args:
    >> file_path (str): The path to the JSON file to parse.

    Returns:
    >> dict: The parsed JSON data as a dictionary.

    Raises:
    >> FileNotFoundError: If the specified file does not exist.
    >> ValueError: If the JSON data is not properly formatted.
    """

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        with open(file_path, 'r') as file:
            json_str = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    return parse_json(json_str)

def loads(json_str: str) -> dict:
    """
    Parses a JSON string into a Python dictionary.

    Args:
    >> json_str (str): The JSON string to parse.

    Returns:
    >> dict: The parsed JSON data as a dictionary.

    Raises:
    >> ValueError: If the JSON data is not properly formatted.
    """

    return parse_json(json_str)

def format(data: dict, level: int = 0, indent: int = 4) -> str:
    """
    Formats a Python dictionary as a JSON string with proper indentation.

    Args:
    >> data (dict): The dictionary to format as JSON.
    >> indent (int): The number of spaces to use for indentation (default is 4).

    Returns:
    >> str: The formatted JSON string.

    Raises:
    >> ValueError: If the data type is not supported.
    """

    try:
        return format_json(data, level, indent)
    except ValueError:
        raise ValueError(f"Unsupported data type: {type(data)}")
    
def dump(data: dict, file_path: str, level: int = 0, indent: int = 4) -> None:
    """
    Formats a Python dictionary as a JSON string and writes it to a file.

    Args:
    >> data (dict): The dictionary to format as JSON.
    >> file_path (str): The path to the file to write the JSON data to.
    >> indent (int): The number of spaces to use for indentation (default is 4).

    Returns:
    >> None

    Raises:
    >> ValueError: If the data type is not supported.
    """

    try:
        json_str = format_json(data, level, indent)
    except ValueError:
        raise ValueError(f"Unsupported data type: {type(data)}")

    with open(file_path, 'w') as file:
        file.write(json_str)