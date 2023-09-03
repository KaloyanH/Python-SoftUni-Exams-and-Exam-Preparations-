from collections import deque

player = deque(input().split(", "))

size = 6

matrix = []

for row in range(size):
    matrix.append(input().split())

rest = {}


while True:

    player_row,  player_col = eval(input())

    if player[0] not in rest:
        rest[player[0]] = "."

    if rest[player[0]] == "x":
        rest[player[0]] = "."
        player.append(player.popleft())
        continue

    if matrix[player_row][player_col] == "E":
        print(f"{player[0]} found the Exit and wins the game!")
        break

    elif matrix[player_row][player_col] == "T":
        print(f"{player[0]} is out of the game! The winner is {player[1]}.")
        break

    elif matrix[player_row][player_col] == "W":
        print(f"{player[0]} hits a wall and needs to rest.")
        rest[player[0]] = "x"

    player.append(player.popleft())


