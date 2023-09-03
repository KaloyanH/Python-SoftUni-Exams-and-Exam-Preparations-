houses = list(map(int, input().split("@")))

current_index = 0
last_position = 0


while True:

    command = input().split()

    if command[0] == "Love!":
        break

    index = int(command[1]) + current_index

    if index >= len(houses):
        index = 0

    if index < len(houses):
        if houses[index] > 0:
            houses[index] -= 2
            if houses[index] == 0:
                print(f"Place {index} has Valentine's day.")
        else:
            print(f"Place {index} already had Valentine's day.")

    current_index = index
    last_position = index


visited_houses = [x for x in houses if x == 0]
diff = abs(len(visited_houses) - len(houses))

print(f"Cupid's last position was {last_position}.")
if len(visited_houses) == len(houses):
    print(f"Mission was successful.")

else:
    print(f"Cupid has failed {diff} places.")

