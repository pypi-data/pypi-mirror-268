def format_json(data: dict, level: int, indent: int = 4) -> str:
    """
    Formats a Python dictionary as a JSON string with proper indentation.

    Args:
    >> data (dict): The dictionary to format as JSON.
    >> level (int): The current indentation level.
    >> indent (int): The number of spaces to use for indentation (default is 4).

    Returns:
    >> str: The formatted JSON string.

    Raises:
    >> ValueError: If the data type is not supported.
    """

    json_str = ""
    indent_str = " " * indent
    next_indent_str = " " * (indent * (level + 1))

    json_str += "{\n"
    for key, value in data.items():
        json_str += f"{next_indent_str}\"{key}\": "
        if isinstance(value, dict):
            # Recursively format nested dictionaries
            json_str += format_json(value, level + 1, indent=indent)
        else:
            json_str += format_value(value)
        json_str += ",\n"
    json_str = json_str[:-2]  # Remove trailing comma and newline
    json_str += f"\n{indent_str * level}}}"

    return json_str

def format_value(value) -> str:
    """
    Formats a value according to its type for JSON representation.

    Args:
    >> value: The value to format.

    Returns:
    >> str: The formatted value as a string.

    Raises:
    >> ValueError: If the data type is not supported.
    """

    if isinstance(value, str):
        return f"\"{value}\""
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif isinstance(value, (int, float)):
        return str(value)
    elif value is None:
        return "null"
    else:
        raise ValueError(f"Unsupported data type: {type(value)}")
