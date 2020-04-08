# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    """

    Args:
        capacity:
        weights:
        prices:

    Returns:

    """
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    current_value = 0.0
    information = {}
    for i in range(len(prices)):
        information[i] = [prices[i], weights[i], prices[i] / weights[i]]
    information = {k: v for k, v in sorted(information.items(), key=lambda info: info[1][2], reverse=True)}

    for key, entry in information.items():
        if capacity != 0:
            if capacity >= entry[1]:
                current_value += entry[0]
                capacity -= entry[1]
                continue
            else:
                current_value += float(capacity * entry[2])
                break
    return current_value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
