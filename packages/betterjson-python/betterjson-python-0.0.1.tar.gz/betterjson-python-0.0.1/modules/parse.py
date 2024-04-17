import re

def parse_json(json_str: str) -> dict:
    """
    Parses a JSON string into a Python dictionary.

    Args:
    >> json_str (str): The JSON string to parse.

    Returns:
    >> dict: The parsed JSON data as a dictionary.

    Raises:
    >> ValueError: If the JSON string is not properly formatted.
    """
    # Strip leading and trailing whitespace
    json_str = json_str.strip()

    # Remove single-line comments
    lines = json_str.split('\n')
    json_str = '\n'.join(line.split('//')[0] for line in lines)

    # Remove multi-line comments
    while '/*' in json_str:
        start_index = json_str.index('/*')
        end_index = json_str.index('*/', start_index) + 2
        json_str = json_str[:start_index] + json_str[end_index:]

    # Check if JSON string is enclosed in curly braces
    if json_str[0] != '{' or json_str[-1] != '}':
        raise ValueError("Incorrect json format")

    # Remove outer curly braces
    json_str = json_str[1:-1]
    parsed_json = {}
    level = 0
    buffer = ""

    inside_array = False
    
    # Iterate through each character in the JSON string
    for char in json_str:
        # Update level for nested objects
        if char == '{':
            level += 1
        elif char == '}':
            level -= 1
        elif char == '[':
            inside_array = True
        elif char == ']':
            inside_array = False

        # Check if at root level, not inside an array, and encountering a comma
        if level == 0 and not inside_array and char == ',':
            # Extract key-value pair
            key_value_pair = buffer.strip()
            index = key_value_pair.find(':')
            if index == -1:
                raise ValueError("Incorrect key-value pair: {}".format(key_value_pair))
            key = key_value_pair[:index].strip().strip('"')
            value = key_value_pair[index + 1:].strip()

            # Check if the value is a mathematical expression
            if re.match(r'^\s*\d+\s*([-+*/]\s*\d+\s*)*$', value):
                value = evaluate_math_expression(value)
            else:
                # Parse value based on data type
                if value[0] == '{' and value[-1] == '}':
                    value = parse_json(value)
                elif value == 'true':
                    value = True
                elif value == 'false':
                    value = False
                elif value[0] == '"' and value[-1] == '"':
                    value = value[1:-1]
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
                            pass

            # Add key-value pair to parsed JSON dictionary
            parsed_json[key] = value

            buffer = ""
        elif char != ' ':
            buffer += char

    # Handle the last key-value pair if buffer is not empty
    if buffer:
        key_value_pair = buffer.strip()
        index = key_value_pair.find(':')
        if index == -1:
            raise ValueError("Incorrect key-value pair: {}".format(key_value_pair))
        key = key_value_pair[:index].strip().strip('"')
        value = key_value_pair[index + 1:].strip()

        # Check if the value is a mathematical expression
        if re.match(r'^\s*\d+\s*([-+*/]\s*\d+\s*)*$', value):
            value = evaluate_math_expression(value)
        else:
            # Parse value based on data type
            if value[0] == '{' and value[-1] == '}':
                value = parse_json(value)
            elif value == 'true':
                value = True
            elif value == 'false':
                value = False
            elif value[0] == '"' and value[-1] == '"':
                value = value[1:-1]
            else:
                try:
                    value = int(value)
                except ValueError:
                    try:
                        value = float(value)
                    except ValueError:
                        pass

        # Add key-value pair to parsed JSON dictionary
        parsed_json[key] = value

    return parsed_json

def evaluate_math_expression(expression: str) -> float:
    """
    Evaluates a mathematical expression and returns the result.

    Args:
    >> expression (str): The mathematical expression to evaluate.

    Returns:
    >> float: The result of the mathematical expression.
    """
    # Replace any occurrence of '+' with ' + ', '-' with ' - ',
    # '*' with ' * ', '/' with ' / ' to ensure proper splitting
    expression = re.sub(r'([-+*/])', r' \1 ', expression)

    # Split the expression by spaces
    tokens = expression.split()

    # Evaluate the expression using eval() function
    return eval(' '.join(tokens))