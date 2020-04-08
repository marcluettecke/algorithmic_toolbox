# python3

from itertools import permutations


def max_dot_product_naive(first_sequence, second_sequence):
    """

    Args:
        first_sequence:
        second_sequence:

    Returns:

    """
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    max_product = 0
    for permutation in permutations(second_sequence):
        dot_product = sum(first_sequence[i] * permutation[i] for i in range(len(first_sequence)))
        max_product = max(max_product, dot_product)

    return max_product


def max_dot_product(first_sequence, second_sequence):
    """

    Args:
        first_sequence:
        second_sequence:

    Returns:

    """
    assert len(first_sequence) == len(second_sequence)
    assert len(first_sequence) <= 10 ** 3
    assert all(0 <= f <= 10 ** 5 for f in first_sequence)
    assert all(0 <= s <= 10 ** 5 for s in second_sequence)

    sorted1 = sorted(first_sequence, reverse=True)
    sorted2 = sorted(second_sequence, reverse=True)
    return sum([i[0] * i[1] for i in zip(sorted1, sorted2)])


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
