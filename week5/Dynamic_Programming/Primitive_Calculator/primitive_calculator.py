# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    min_steps = {1: [0, [1]]}
    for m in range(2, n + 1):
        min_steps[m] = [float("inf"), []]

        for index, value in enumerate([m - 1, m / 2, m / 3]):
            if index == 1:
                if m % 2 != 0:
                    continue
            if index == 2:
                if m % 3 != 0:
                    continue
            lower_value = value

            if lower_value > 0:
                num_steps = min_steps[lower_value][0] + 1
                intermediate_list = min_steps[lower_value][1] + [m]
                if num_steps < min_steps[m][0]:
                    min_steps[m][0] = num_steps
                    min_steps[m][1] = intermediate_list

    return min_steps[n][1]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)

