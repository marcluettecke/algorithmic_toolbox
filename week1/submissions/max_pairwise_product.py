# python3
from functools import reduce
from operator import mul


def max_pairwise_product_naive(numbers):
    """
    Naive and slow implementation of function for testing purposes
    Args:
        numbers: input of numbers

    Returns:
        int: product of two largest elements of array
    """
    assert len(numbers) >= 2
    assert all(0 <= x <= 2 * 10 ** 5 for x in numbers)

    product = 0

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            product = max(product, numbers[i] * numbers[j])

    return product


def max_pairwise_product(numbers):
    """
    Method to return the product of the two largest numbers of array in linear time.
    Args:
        numbers: input of numbers

    Returns:
        int: product of two largest elements of array
    """
    return reduce(mul, sorted([int(x) for x in numbers])[-2:], 1)


if __name__ == '__main__':
    n = int(input())
    input_numbers = list(map(int, input().split()))
    assert len(input_numbers) == n
    print(max_pairwise_product(input_numbers))
