# python3

from itertools import permutations


def largest_number_naive(numbers):
    """
    Naive algorithm that tests all possible combinations of numbers until it finds the max.
    Args:
        numbers: list of numbers to be concatenated

    Returns:
        largest possible integer
    """
    numbers = list(map(str, numbers))

    largest = 0

    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    """
    Efficient solution to convert the numbers into strings, then find the max len of the longest integer, padd
    Args:
        numbers: list of numbers to be concatenated

    Returns:
        largest possible integer
    """
    snippets = [str(s) for s in numbers]
    mlen = max(len(s) for s in snippets) * 2
    return int(''.join(sorted(snippets, reverse=True, key=lambda s: s * (mlen // len(s) + 1))))


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
