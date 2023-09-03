def check_traverse(r, c, rows, cols):
    if r < 0:
        return rows - 1, c

    elif r >= rows:
        return 0, c

    elif c < 0:
        return r, cols - 1

    elif c >= cols:
        return r, 0

    else:
        return r, c


def move_up(r, c):
    return r - 1, c


def move_down(r, c):
    return r + 1, c


def move_left(r, c):
    return r, c - 1


def move_right(r, c):
    return r, c + 1


rows, cols = [int(x) for x in input().split(", ")]

decorations = 0
gifts = 0
cookies = 0
position = []

matrix = []

directions = {

    "up": move_up,
    "down": move_down,
    "left": move_left,
    "right": move_right

}

for row in range(rows):
    matrix.append(input().split())
    for col in range(cols):
        if matrix[row][col] == "Y":
            position.append(row)
            position.append(col)
        if matrix[row][col] == "D":
            decorations += 1
        if matrix[row][col] == "G":
            gifts += 1
        if matrix[row][col] == "C":
            cookies += 1

curr_decs = 0
curr_gifts = 0
curr_cookies = 0
gifts_collected = False

command = input().split("-")

matrix[position[0]][position[1]] = "x"

while command[0] != "End":

    steps = int(command[1])

    for step in range(steps):

        row, col = directions[command[0]](position[0], position[1])
        row, col = check_traverse(row, col, rows, cols)
        if matrix[row][col] == "D":
            curr_decs += 1
        elif matrix[row][col] == "G":
            curr_gifts += 1
        elif matrix[row][col] == "C":
            curr_cookies += 1
        position[0], position[1] = row, col
        matrix[row][col] = "x"

        if curr_cookies == cookies and curr_decs == decorations and curr_gifts == gifts:
            gifts_collected = True
            break
    if gifts_collected:
        break

    command = input().split("-")

matrix[position[0]][position[1]] = "Y"

if gifts_collected:
    print(f"Merry Christmas!")
print(f"You've collected:")
print(f"- {curr_decs} Christmas decorations")
print(f"- {curr_gifts} Gifts")
print(f"- {curr_cookies} Cookies")
for row in matrix:
    print(*row, sep=" ")
