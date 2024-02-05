from pprint import pp


def f(row: int, col: int):
    matrix = [[0 for _ in range(col)] for _ in range(row)]

    for i in range(row):
        matrix[i][col - 1] = 1

    for i in range(col):
        matrix[row - 1][i] = 1

    

    return matrix


print(f(3, 7))
# [
# [0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 1],
# ]
