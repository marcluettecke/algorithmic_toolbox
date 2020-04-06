
def gcd(a, b):
    """
    Uses the Euclidian algorithm to solve the gcd problem
    Args:
        a: number one int
        b:number two int

    Returns:
        The greatest common divisor of a and b
    """
    assert 0 <= a <= 2 * 10 ** 9 and 0 <= b <= 2 * 10 ** 9

    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b


def lcm_naive(a, b):
    """
    Naive implementation finding the least common multiple utilizing brute force.
    Args:
        a: integer 1
        b:integer 2

    Returns:
        lcm of a and b
    """
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    multiple = max(a, b)
    while multiple % a != 0 or multiple % b != 0:
        multiple += 1

    return multiple


def lcm(a, b):
    """
    Efficient implementation finding the least common multiple utilizing the greatest common factor.
    Args:
        a: integer 1
        b:integer 2

    Returns:
        lcm of a and b
    """
    assert 1 <= a <= 2 * 10 ** 9 and 1 <= b <= 2 * 10 ** 9

    return int((a * b) / gcd(a, b))


if __name__ == '__main__':
    input_a, input_b = map(int, input().split())
    print(lcm(input_a, input_b))
