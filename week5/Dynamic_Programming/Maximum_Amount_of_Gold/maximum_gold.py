# python3

from sys import stdin


def maximum_gold(capacity, weights):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(weights) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in weights)
    value = [[0] * (capacity + 1) for _ in range(len(weights) + 1)]
    n = len(weights)
    for item_index, item_value in enumerate(weights):
        item_index += 1
        for weight in range(1, capacity + 1):
            value[item_index][weight] = value[item_index-1][weight]
            if item_value <= weight:
                val = value[item_index - 1][weight - item_value] + item_value
                if value[item_index][weight] < val:
                    value[item_index][weight] = val

    return value[n][capacity]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n
    print(maximum_gold(input_capacity, input_weights))
