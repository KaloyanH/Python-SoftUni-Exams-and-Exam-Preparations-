def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def move_up(r, c):
    return r - 1, c


def move_down(r, c):
    return r + 1, c


def move_left(r, c):
    return r, c - 1


def move_right(r, c):
    return r, c + 1


def right_dia_up(r, c):
    return r - 1, c + 1


def left_dia_up(r, c):
    return r - 1, c - 1


def right_dia_down(r, c):
    return r + 1, c + 1


def left_dia_down(r, c):
    return r + 1, c - 1


size = 8

matrix = []

king_pos = []
queen_pos = []
mate_pos = []

for row in range(size):
    matrix.append(input().split())

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "K":
            king_pos.append((row, col))

        elif matrix[row][col] == "Q":
            queen_pos.append((row, col))

directions = {

    "up": move_up,
    "down": move_down,
    "left": move_left,
    "right": move_right,
    "right_diagonal_up": right_dia_up,
    "left_diagonal_up": left_dia_up,
    "right_diagonal_down": right_dia_down,
    "left_diagonal_down": left_dia_down
}


met_king = False

for queens in queen_pos:

    for direction in directions:

        row = queens[0]
        col = queens[1]

        while True:

            met_king = False

            next_row, next_col = directions[direction](row, col)

            if not is_inside(next_row, next_col, size):
                break

            if matrix[next_row][next_col] == ".":
                row, col = next_row, next_col
                continue

            if matrix[next_row][next_col] == "Q":
                break

            if matrix[next_row][next_col] == "K":
                mate_pos.append((queens[0], queens[1]))
                met_king = True
                break

        if met_king:
            break

if mate_pos:
    for el in mate_pos:
        print(f"[{el[0]}, {el[1]}]")
else:
    print(f"The king is safe!")
