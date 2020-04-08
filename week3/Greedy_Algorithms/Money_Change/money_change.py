# python3


def money_change(money):
    """

    Args:
        money:

    Returns:

    """
    assert 0 <= money <= 10 ** 3
    n_coins = int(money / 10)
    n_coins += int(money % 10 / 5)
    return n_coins + (money % 10) % 5


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
