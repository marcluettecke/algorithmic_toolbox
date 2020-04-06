# python3

def modulo10(integer):
    """
    Applies modulo 10 to number
    Args:
        integer: number to apply the operation to

    Returns:
        remainder after dividing the number by 10
    """

    return integer % 10


def last_digit_sequence_sum():
    """
    Returns the repeating sequence of the last digits of the Fibonacci numbers (60 elements)
    Returns:
        list with last digits
    """
    initial_values = [0, 1]
    for i in range(2, 60):
        initial_values.append(sum([initial_values[i - 2], initial_values[i - 1]]))
    running_sums = [sum(initial_values[:i]) for i in range(1, len(initial_values)+1)]
    # print(list(map(modulo10, running_sums)))
    return list(map(modulo10, running_sums))



def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    """

    Args:
        n:

    Returns:

    """
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    """

    Args:
        n:

    Returns:

    """
    assert 0 <= n <= 10 ** 18
    sequence_of_digits = last_digit_sequence_sum()
    return sequence_of_digits[n % 60]


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
