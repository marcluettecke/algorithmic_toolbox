# python3
import sys


def linear_search(keys, query):
    """
    
    Args:
        keys: 
        query: 

    Returns:

    """
    for i in range(len(keys)):
        if keys[i] == query:
            return i

    return -1


def binary_search(a, x):
    """
    Runs the implementatiion below with initialized lower and upper bound.
    Args:
        a: sorted array
        x: target to be found in array

    Returns:
        index of target in array
    """
    left, right = 0, (len(a) - 1)
    return binary_search_run(a, left, right, x)

def binary_search_run(a, left, right, x):
    """
    Implements the actual calculation procedures of the binary search algorithm efficiently
    Args:
        a: sorted array
        left: left most element
        right: right most element
        x: target to be found

    Returns:
        recursive call of binary search function which eventually returns the index, when it equals the mid element

    """
    if right < left:
        return -1
    mid = int(left + (right - left) / 2)
    if x == a[mid]:
        return mid
    elif x > a[mid]:
        return binary_search_run(a, mid + 1, right, x)
    else:
        return binary_search_run(a, left, mid-1, x)


if __name__ == '__main__':
    input1 = sys.stdin.read()
    data = list(map(int, input1.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end=" ")
