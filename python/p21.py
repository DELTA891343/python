def find_length(string):
    """
    Finds and returns the length of the given string.

    :param string: The input string.
    :return: The length of the string as an integer.
    """
    length = 0
    for _ in string:
        length += 1
    return length

# Example usage
user_input = input("Enter a string: ")
length = find_length(user_input)
print(f"The length of the string '{user_input}' is: {length}")
