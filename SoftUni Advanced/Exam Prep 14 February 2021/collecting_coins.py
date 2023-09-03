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


directions = {

    "up": move_up,
    "down": move_down,
    "left": move_left,
    "right": move_right

}


size = int(input())

matrix = []

player_row = 0
player_col = 0

walls_pos = []

for row in range(size):
    matrix.append(input().split())
    for col in range(size):
        if matrix[row][col] == "P":
            player_row = row
            player_col = col
        if matrix[row][col] == "X":
            walls_pos.append((row, col))
matrix[player_row][player_col] = "-"

coins = 0
winning_path = [(player_row, player_col)]
hit_a_wall = False

while coins < 100:

    command = input()

    if command in directions.keys():
        new_row, new_col = directions[command](player_row, player_col)

        if not is_valid(new_row, new_col, size):
            new_row, new_col = traverse(new_row, new_col, size)

        if matrix[new_row][new_col] == "-":
            player_row, player_col = new_row, new_col
            winning_path.append((new_row, new_col))
            continue

        if matrix[new_row][new_col] == "X":
            winning_path.append((new_row, new_col))
            coins = int(coins/2)
            hit_a_wall = True
            break

        coins += int(matrix[new_row][new_col])
        winning_path.append((new_row, new_col))
        matrix[new_row][new_col] = "-"
        player_row, player_col = new_row, new_col

    else:
        continue

if hit_a_wall:
    print(f"Game over! You've collected {coins} coins.")
else:
    print(f"You won! You've collected {coins} coins.")
print(f"Your path: ")
for row in winning_path:
    print(f"[{row[0]}, {row[1]}]")
