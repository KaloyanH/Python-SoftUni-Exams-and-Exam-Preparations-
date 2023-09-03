elements = input().split()
moves = 0

while True:
    command = input()

    if command == "end":
        break
    if len(elements) == 0:
        break

    moves += 1
    current_command = command.split()
    first_index = int(current_command[0])
    second_index = int(current_command[1])

    if first_index == second_index or first_index < 0 or first_index >= len(elements) \
            or second_index < 0 or second_index >= len(elements):
        print(f"Invalid input! Adding additional elements to the board")
        middle_index = len(elements) // 2
        elements = elements[:middle_index] + [f"-{moves}a", f"-{moves}a"] + elements[middle_index:]
        continue

    elif elements[first_index] == elements[second_index]:
        removed_element = elements.pop(first_index)
        elements.remove(removed_element)
        print(f"Congrats! You have found matching elements - {removed_element}!")

    elif elements[first_index] != elements[second_index]:
        print(f"Try again!")
        continue

if len(elements) == 0:
    print(f"You have won in {moves} turns!")

else:
    print("Sorry you lose :(")
    print(" ".join(elements))
