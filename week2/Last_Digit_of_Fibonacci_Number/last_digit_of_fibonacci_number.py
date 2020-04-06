# python3


def last_digit_of_fibonacci_number_naive(n):
    """
    Naive implementation to find last digit of Fibonacci element at position n
    Args:
        n: element index

    Returns:
        int of last digit of element at Fibonacci sequence at index n
    """
    assert 0 <= n <= 10 ** 7

    if n <= 1:
        return n

    return (last_digit_of_fibonacci_number_naive(n - 1) + last_digit_of_fibonacci_number_naive(n - 2)) % 10


def last_digit_sequence():
    """
    Returns the repeating sequence of the last digits of the Fibonacci numbers (60 elements)
    Returns:
        list with last digits
    """
    initial_values = [0, 1]
    for i in range(2, 60):
        initial_values.append(sum([initial_values[i - 2], initial_values[i - 1]]))
    return list(map(modulo10, initial_values))


def modulo10(integer):
    """
    Applies modulo 10 to number
    Args:
        integer: number to apply the operation to

    Returns:
        remainder after dividing the number by 10
    """

    return integer % 10


def last_digit_of_fibonacci_number(n):
    """
    Efficient implementation to find last digit of Fibonacci number.
    Args:
        n: length of Fibonacci sequence

    Returns:
        int of last digit
    """
    assert 0 <= n <= 10 ** 7
    sequence_of_digits = last_digit_sequence()
    return sequence_of_digits[n % 60]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_fibonacci_number(input_n))
