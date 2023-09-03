def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True


def traverse(r, c, size):
    if r < 0:
        return size - 1, c

    elif r >= size:
        return 0, c

    elif c < 0:
        return r, size - 1

    elif c >= size:
        return r, 0


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

rover_row = 0
rover_col = 0

movement = {

    "up": move_up,
    "down": move_down,
    "left": move_left,
    "right": move_right

}

for row in range(size):
    matrix.append(input().split())

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "E":
            rover_row = row
            rover_col = col

deposits = {

    "water": 0,
    "metal": 0,
    "concrete": 0

}

commands = input().split(", ")

for command in commands:

    if command in movement.keys():
        new_row, new_col = movement[command](rover_row, rover_col)

        if not is_valid(new_row, new_col, size):
            new_row, new_col = traverse(new_row, new_col, size)

        if matrix[new_row][new_col] == "W":
            deposits["water"] += 1
            print(f"Water deposit found at ({new_row}, {new_col})")

        if matrix[new_row][new_col] == "M":
            deposits["metal"] += 1
            print(f"Metal deposit found at ({new_row}, {new_col})")

        if matrix[new_row][new_col] == "C":
            deposits["concrete"] += 1
            print(f"Concrete deposit found at ({new_row}, {new_col})")

        if matrix[new_row][new_col] == "R":
            print(f"Rover got broken at ({new_row}, {new_col})")
            break

        rover_row, rover_col = new_row, new_col


if all(x >= 1 for x in deposits.values()):
    print(f"Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")

