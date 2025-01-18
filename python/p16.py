def fibonacci_series(n):
    """
    Prints the Fibonacci series up to N numbers.

    :param n: An integer representing the number of terms in the series.
    """
    if n <= 0:
        print("Please enter a positive integer.")
        return

    # Initialize the first two Fibonacci numbers
    a, b = 0, 1

    print(f"Fibonacci series up to {n} terms:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  # For a new line after printing the series

# Example usage
N = int(input("Enter the number of terms for the Fibonacci series: "))
fibonacci_series(N)