def move_up(r, c):
    return r - 1, c


def move_down(r, c):
    return r + 1, c


def move_left(r, c):
    return r, c - 1


def move_right(r, c):
    return r, c + 1


size_of_matrix = int(input())
race_car_number = input()

matrix = []


for row in range(size_of_matrix):
    matrix.append(input().split())

car_row = 0
car_col = 0
tunnels_pos = []


for row in range(size_of_matrix):
    for col in range(size_of_matrix):
        if matrix[row][col] == "T":
            tunnels_pos.append((row, col))


directions = {

    "up": move_up,
    "down": move_down,
    "left": move_left,
    "right": move_right

}

total_kms = 0
finished_the_race = False

command = input()

while command != "End":

    new_row, new_col = directions[command](car_row, car_col)

    if matrix[new_row][new_col] == ".":
        total_kms += 10
        car_row, car_col = new_row, new_col

    elif matrix[new_row][new_col] == matrix[tunnels_pos[0][0]][tunnels_pos[0][1]]:
        total_kms += 30
        matrix[tunnels_pos[0][0]][tunnels_pos[0][1]] = "."
        car_row, car_col = tunnels_pos[1][0], tunnels_pos[1][1]
        matrix[tunnels_pos[1][0]][tunnels_pos[1][1]] = "."

    elif matrix[new_row][new_col] == matrix[tunnels_pos[1][0]][tunnels_pos[1][1]]:
        total_kms += 30
        matrix[tunnels_pos[1][0]][tunnels_pos[1][1]] = "."
        car_row, car_col = tunnels_pos[0][0], tunnels_pos[0][1]
        matrix[tunnels_pos[0][0]][tunnels_pos[0][1]] = "."

    elif matrix[new_row][new_col] == "F":
        car_row, car_col = new_row, new_col
        total_kms += 10
        finished_the_race = True
        break

    command = input()

matrix[car_row][car_col] = "C"

if finished_the_race:
    print(f"Racing car {race_car_number} finished the stage!")
else:
    print(f"Racing car {race_car_number} DNF.")

print(f"Distance covered {total_kms} km.")

for row in matrix:
    print(*row, sep="")
