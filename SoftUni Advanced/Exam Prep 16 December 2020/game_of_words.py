def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True


def move_up(r, c):
    return r - 1, c


def move_down(r, c):
    return r + 1, c


def move_left(r, c):
    return r, c - 1


def move_right(r, c):
    return r, c + 1


initial_string = input()

size = int(input())

matrix = []
player_position = []

directions = {

    "up": move_up,
    "down": move_down,
    "left": move_left,
    "right": move_right

}


for row in range(size):
    matrix.append(list(input()))
    for col in range(size):
        if matrix[row][col] == "P":
            player_position.append((row, col))

moves = int(input())

player_row = player_position[0][0]
player_col = player_position[0][1]

matrix[player_row][player_col] = "-"

for move in range(moves):

    current_move = input()

    if current_move in directions.keys():

        new_row, new_col = directions[current_move](player_row, player_col)

        if not is_valid(new_row, new_col, size):
            initial_string = initial_string[:-1]
            continue

        player_row, player_col = new_row, new_col

        symbol = matrix[new_row][new_col]

        if symbol.isalpha():
            initial_string += matrix[new_row][new_col]
            matrix[new_row][new_col] = "-"


matrix[player_row][player_col] = "P"

print(initial_string)
for row in matrix:
    print(*row, sep="")
