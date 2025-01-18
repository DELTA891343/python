def find_odd_even(n):
    """
    Finds and prints odd and even numbers from 1 to N.

    :param n: An integer representing the range limit.
    """
    if n <= 0:
        print("Please enter a positive integer greater than 0.")
        return

    # Lists to store odd and even numbers
    odd_numbers = []
    even_numbers = []

    for i in range(1, n + 1):
        if i % 2 == 0:
            even_numbers.append(i)
        else:
            odd_numbers.append(i)

    # Print the results
    print(f"Even numbers from 1 to {n}: {even_numbers}")
    print(f"Odd numbers from 1 to {n}: {odd_numbers}")

# Example usage
N = int(input("Enter the value of N: "))
find_odd_even(N)
