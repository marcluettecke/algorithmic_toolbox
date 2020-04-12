# python3


def change_naive(money):
    """
    Naive solution using brute force to find number of coins necessary to change money.
    Args:
        money: integer for which you need change

    Returns:
        Number of coins (from [1, 3, 4]) to split up money.
    """
    min_coins = float("inf")

    for num1 in range(money + 1):
        for num3 in range(money // 3 + 1):
            for num4 in range(money // 4 + 1):
                if 1 * num1 + 3 * num3 + 4 * num4 == money:
                    min_coins = min(min_coins, num1 + num3 + num4)

    return min_coins


def change(money):
    """
    Dynamic programming solution to money change problem, which overcomes common problems of the greedy approach.
    Args:
        money: integer for which you need change

    Returns:
        Number of coins (from [1, 3, 4]) to split up money.
    """
    # set up coins list
    coins = [1, 3, 4]
    # initiate dictionary to hold values
    min_num_coins = {0: 0}
    # build the dictionary from 1 to money amount
    for m in range(1, money + 1):
        # first set infinity as value
        min_num_coins[m] = float('inf')
        # iterate through the coin options
        for i in coins:
            # if the current value is larger than the current coin use last values number of coins and add 1
            if m >= i:
                num_coins = min_num_coins[m - i] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins
    return min_num_coins[money]


if __name__ == '__main__':
    amount = int(input())
    print(change(amount))
