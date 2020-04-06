# python3


def gcd_naive(a, b):
    """
    Naive (slow) algorithm to solve the gcd problem
    Args:
        a: number one int
        b:number two int

    Returns:
        The greates common divisor of a and b
    """
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    for divisor in range(min(a, b), 0, -1):
        if a % divisor == 0 and b % divisor == 0:
            return divisor

    assert False


def gcd(a, b):
    """
    Uses the Euclidian algorithm to solve the gcd problem
    Args:
        a: number one int
        b:number two int

    Returns:
        The greates common divisor of a and b
    """
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(gcd(input_a, input_b))
