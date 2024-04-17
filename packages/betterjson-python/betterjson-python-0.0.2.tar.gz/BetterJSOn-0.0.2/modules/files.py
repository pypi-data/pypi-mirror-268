def save_to_file(file_path: str, data: dict) -> None:
    """
    Saves a dictionary as JSON to a file.

    Args:
    >> file_path (str): The path to the file where the JSON will be saved.
    >> data (dict): The dictionary to save as JSON.

    Returns:
    >> None

    Raises:
    >> FileNotFoundError: If the specified directory for the file does not exist.
    >> PermissionError: If the user does not have permission to write to the specified file.
    >> TypeError: If the data to be saved is not a dictionary.
    """

    if not isinstance(data, dict):
        raise TypeError("Data must be a dictionary.")

    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except FileNotFoundError:
        raise FileNotFoundError(f"Directory does not exist: {file_path}")
    except PermissionError:
        raise PermissionError(f"Permission denied: {file_path}")
