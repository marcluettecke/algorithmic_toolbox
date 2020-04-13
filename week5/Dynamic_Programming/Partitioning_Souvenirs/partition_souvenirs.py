# python3

from itertools import product
from sys import stdin


def partition3(values, number_of_partitions: int = 3):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)
    len_values = len(values)
    sum_values = sum(values)
    sum_per_person = sum_values // number_of_partitions
    if sum_values % number_of_partitions != 0:
        return 0

    D = [[0] * (len_values + 1) for _ in range(sum_per_person + 1)]

    count = 0

    for i in range(1, sum_per_person + 1):
        for j in range(1, len_values + 1):
            D[i][j] = D[i][j - 1]
            if values[j - 1] <= i:
                temp_val = D[i - values[j - 1]][j - 1] + values[j - 1]
                if temp_val >= D[i][j]:
                    D[i][j] = temp_val
                    if D[i][j] == sum_per_person:
                        count += 1
    if count < 3:
        return 0
    else:
        return 1


if __name__ == '__main__':
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))
