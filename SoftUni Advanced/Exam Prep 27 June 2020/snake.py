def border_check(curr_row, curr_col):
    if curr_row >= size or curr_row < 0 or curr_col >= size or curr_col < 0:
        return True


size = int(input())

matrix = []

snake_pos = []
burrow_pos = []

directions = {

    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for _ in range(size):
    matrix.append(list(input()))


for row in range(size):
    for col in range(size):
        if matrix[row][col] == "S":
            snake_pos.append(row)
            snake_pos.append(col)
        elif matrix[row][col] == "B":
            burrow_pos.append((row, col))

food_eaten = 0
going_out = False

matrix[snake_pos[0]][snake_pos[1]] = "."

while True:

    if food_eaten >= 10:
        matrix[snake_pos[0]][snake_pos[1]] = "S"
        break

    cmd = input()

    new_row, new_col = (snake_pos[0] + directions[cmd][0]), (snake_pos[1] + directions[cmd][1])

    if border_check(new_row, new_col):
        going_out = True
        break

    snake_pos[0], snake_pos[1] = new_row, new_col

    if matrix[new_row][new_col] == "*":
        food_eaten += 1
        matrix[new_row][new_col] = "."

    elif matrix[new_row][new_col] == "-":
        matrix[new_row][new_col] = "."

    elif matrix[new_row][new_col] == matrix[burrow_pos[0][0]][burrow_pos[0][1]]:
        matrix[burrow_pos[0][0]][burrow_pos[0][1]] = "."
        snake_pos[0], snake_pos[1] = burrow_pos[1][0], burrow_pos[1][1]
        matrix[burrow_pos[1][0]][burrow_pos[1][1]] = "."

    elif matrix[new_row][new_col] == matrix[burrow_pos[1][0]][burrow_pos[1][1]]:
        matrix[burrow_pos[1][0]][burrow_pos[1][1]] = "."
        snake_pos[0], snake_pos[1] = burrow_pos[0][0], burrow_pos[0][1]
        matrix[burrow_pos[0][0]][burrow_pos[0][1]] = "."

if going_out:
    print(f"Game over!")

if food_eaten >= 10:
    print(f"You won! You fed the snake.")

print(f"Food eaten: {food_eaten}")

for row in matrix:
    print(*row, sep="")



