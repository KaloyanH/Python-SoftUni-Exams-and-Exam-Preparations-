from collections import deque


def is_valid(r, c, size):
    if 0 <= r < size and 0 <= c < size:
        return True


def multiply_points(r, c, matrix):
    total_sum = 0
    for el in matrix[r]:
        if el.isdigit():
            total_sum += int(el)
    total_sum += sum(int(r[c]) for r in matrix if r[c].isdigit())
    return total_sum


players = deque([name for name in input().split(", ")])

dartboard = []

size = 7

for _ in range(size):
    dartboard.append(input().split())

bulls_eye = []

points_dict = {}
throws_dict = {}

while True:

    current_player = players[0]

    if current_player not in points_dict:
        points_dict[current_player] = 501
        throws_dict[current_player] = 0

    coordinates = eval(input())
    row, col = coordinates[0], coordinates[1]

    if not is_valid(row, col, size):
        throws_dict[current_player] += 1
        players.append(players.popleft())
        continue

    throws_dict[current_player] += 1

    if dartboard[row][col] == "B":
        break

    elif dartboard[row][col] == "D":
        points_dict[current_player] -= 2 * multiply_points(row, col, dartboard)

    elif dartboard[row][col] == "T":
        points_dict[current_player] -= 3 * multiply_points(row, col, dartboard)

    else:
        points_dict[current_player] -= int(dartboard[row][col])

    if any(points <= 0 for points in points_dict.values()):
        break

    players.append(players.popleft())

print(f"{players[0]} won the game with {throws_dict[current_player]} throws!")
