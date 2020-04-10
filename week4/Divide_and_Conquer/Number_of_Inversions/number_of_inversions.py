# python3
import sys
from itertools import combinations


def compute_inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions


def merge(b, c):
    """Merge procedure.
    Returns the resulting sorted array and the number inversions.
    An inversion of a sequence a[0], a[1], ... , a[n−1] is a pair of indices
    0 ≤ i < j < n such that a[i] > a[j] . The number of inversions of a sequence
    in some sense measures how close the sequence is to being sorted.
    Samples:
    '>>> b = [1, 2, 3, 4, 5]'
    '>>> c = [3, 5, 6, 8, 9]'
    '>>> merge(b, c)'
    ([1, 2, 3, 3, 4, 5, 5, 6, 8, 9], 2)
    """
    result = []
    inversions = 0
    while b and c:
        if b[0] <= c[0]:
            result.append(b.pop(0))
        else:
            result.append(c.pop(0))
            inversions += len(b)
    # append all remaining values of b or c
    result += b or c
    return result, inversions


def merge_sort(a):
    """
    Implement the merge sort algorithm and return number of inversions
    Args:
        a: unsorted array, such as [1,2,5,4]

    Returns:
        sorted array, number of inversions: [1,2,4,5], 1
    """

    if len(a) == 1:
        return a, 0

    mid = len(a) // 2
    left, left_inv = merge_sort(a[:mid])
    right, right_inv = merge_sort(a[mid:])

    merged, merged_inv = merge(left, right)
    return merged, merged_inv + left_inv + right_inv


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(merge_sort(a)[1])
