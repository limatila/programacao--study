"""
Generate the Fibonacci sequence up to the given number of terms.

Args:
    n (int): The number of terms in the Fibonacci sequence to generate.

Returns:
    None: This function does not return anything.
    It prints the Fibonacci sequence to the console.

Example:
    >>> fibonacci_sequence(5)
    0, 1, 1, 2, 3
"""


def fibonacci_sequence(n: int) -> None:
    last, present = 0, 1
    for _ in range(n):
        print(last, end=', ')
        last, present = present, last + present  # present becomes last


if __name__ == '__main__':
    fibonacci_sequence(10)
