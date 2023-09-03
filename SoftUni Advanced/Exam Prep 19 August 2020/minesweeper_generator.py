def find_bombs(matrix, row, col):
    moves = [

        [row, col - 1],
        [row, col + 1],
        [row + 1, col],
        [row - 1, col],
        [row - 1, col - 1],
        [row - 1, col + 1],
        [row + 1, col - 1],
        [row + 1, col + 1]
    ]

    result = 0
    for r, c in moves:
        if 0 <= r < len(matrix) and 0 <= c < len(matrix) and matrix[r][c] == "*":
            result += 1
    return result


size = int(input())
bombs = int(input())

matrix = []
bomb_pos = []

for _ in range(size):
    matrix.append(list(size * "-"))

for bomb in range(bombs):
    bomb_pos.append(eval(input()))

for bomb in bomb_pos:
    for row in range(size):
        for col in range(size):
            matrix[bomb[0]][bomb[1]] = "*"

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "*":
            continue

        cell_size = find_bombs(matrix, row, col)
        matrix[row][col] = cell_size

for row in matrix:
    print(*row)
