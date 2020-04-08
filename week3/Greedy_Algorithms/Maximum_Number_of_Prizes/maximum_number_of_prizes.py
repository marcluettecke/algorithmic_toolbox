# python3
def compute_optimal_summands(n):
    """
    Method to find the largest possible split of a number into sum of integers
    Args:
        n: the resulting sum

    Returns:
        list of integers
    """
    assert 1 <= n <= 10 ** 9
    summands = []
    initial_value = n
    sum = 0
    if n == 1:
        return [1]
    for i in range(1, int(n/2)+1):
        if n >= 0:
            if i <= n:
                summands.append(i)
                n -= i
                sum += i
        else:
            break
    summands[-1] = initial_value-(sum-summands[-1])
    return summands


if __name__ == '__main__':
    input_n = int(input())
    output_summands = compute_optimal_summands(input_n)
    print(len(output_summands))
    print(*output_summands)
    # compute_optimal_summands(6)
