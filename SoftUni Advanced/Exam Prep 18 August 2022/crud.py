def move_up(r, c):
    return r - 1, c


def move_down(r, c):
    return r + 1, c


def move_left(r, c):
    return r, c - 1


def move_right(r, c):
    return r, c + 1


size = 6

matrix = []

for row in range(size):
    matrix.append(input().split())

movement = {

    "up": move_up,
    "down": move_down,
    "left": move_left,
    "right": move_right

}

start_row, start_col = eval(input())

while True:

    cmd = input().split(", ")

    if cmd[0] == "Stop":
        break

    new_row, new_col = movement[cmd[1]](start_row, start_col)

    if cmd[0] == "Create":
        if matrix[new_row][new_col] == ".":
            matrix[new_row][new_col] = cmd[2]

    elif cmd[0] == "Update":
        if matrix[new_row][new_col] != ".":
            matrix[new_row][new_col] = cmd[2]

    elif cmd[0] == "Delete":
        if matrix[new_row][new_col] != ".":
            matrix[new_row][new_col] = "."

    elif cmd[0] == "Read":
        if matrix[new_row][new_col] != ".":
            print(matrix[new_row][new_col])

    start_row, start_col = new_row, new_col

for row in matrix:
    print(*row, sep=" ")
