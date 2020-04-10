# python3
import sys


def majority_element_naive(elements):
    """

    Args:
        elements:

    Returns:

    """
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1

    return 0


def majority_element(array):
    """
    Majority Element.
    An element of a sequence of length n is called a majority element if
    it appears in the sequence strictly more than n/2 times.
    Args:
        array:

    Returns:

    """

    # The task is solved using Boyer–Moore majority vote algorithm.
    right = len(array)
    maj_index = 0
    count = 1
    # it has to increase more than decrease
    for i in range(1, right):

        if array[i] == array[maj_index]:
            count += 1
        else:
            count -= 1

        if count == 0:
            maj_index = i
            count = 1

    count = 0
    # count occurences and check if majority overall
    for i in range(right):
        if array[i] == array[maj_index]:
            count += 1

    if count > right // 2:
        return 1
    return 0


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(majority_element(a))
