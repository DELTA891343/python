def reverse_value(value):
    """
    Reverses the given value (string or integer).

    :param value: The value to be reversed.
    :return: The reversed value.
    """
    # Convert to string to handle integers or other types
    value_str = str(value)
    reversed_value = value_str[::-1]
    return reversed_value

# Example usage
user_input = input("Enter a value to reverse: ")

# Reverse the value and display the result
reversed_result = reverse_value(user_input)
print(f"The reversed value is: {reversed_result}")
