def factorial(number):
    """
    Calculates the factorial of a given number.

    :param number: A non-negative integer.
    :return: The factorial of the number.
    """
    if number < 0:
        return "Factorial is not defined for negative numbers."
    elif number == 0 or number == 1:
        return 1
    else:
        result = 1
        for i in range(2, number + 1):
            result *= i
        return result

# Example usage
num = int(input("Enter a number to find its factorial: "))

fact = factorial(num)
print(f"The factorial of {num} is: {fact}")
