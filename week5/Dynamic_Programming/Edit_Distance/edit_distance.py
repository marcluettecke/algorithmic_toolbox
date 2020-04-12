# python3


def edit_distance(first_string, second_string):
    # append the necessary 0 empty padding
    first_string, second_string = "0" + first_string, "0" + second_string
    # prepare scoring board
    D = [[0 for _ in range(len(first_string))] for _ in range(len(second_string))]
    # fill the first row of the board with the subsequent insertion scores
    for i in range(1, len(first_string)):
        D[0][i] = i
    # transpose and fill values of first entry of each column before tranposing back
    D = list(map(list, zip(*D)))
    for j in range(1, len(second_string)):
        D[0][j] = j
    D = list(map(list, zip(*D)))

    # iterate through the two strings and fill the board D with the best score
    for index2 in range(1, len(list(second_string))):
        for index1 in range(1, len(list(first_string))):
            insertion = D[index2][index1 - 1] + 1
            deletion = D[index2 - 1][index1] + 1
            match = D[index2 - 1][index1 - 1]
            mismatch = D[index2 - 1][index1 - 1] + 1

            if list(first_string)[index1] == list(second_string)[index2]:
                D[index2][index1] = min(insertion, deletion, match)
            else:
                D[index2][index1] = min(insertion, deletion, mismatch)
    return D[len(list(second_string))-1][len(list(first_string))-1]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
    # print(edit_distance("short", "ports"))
