current_array = input().split()

while True:
    command = input()

    if command == "end":
        break

    current_cmd = command.split()

    if current_cmd[0] == "swap":
        first_index = int(current_cmd[1])
        second_index = int(current_cmd[2])
        current_array[first_index], current_array[second_index] = \
            current_array[second_index], current_array[first_index]

    elif current_cmd[0] == "multiply":
        first_num = int(current_cmd[1])
        second_num = int(current_cmd[2])
        multiplication = int(current_array[first_num]) * int(current_array[second_num])
        current_array[first_num] = multiplication

    elif current_cmd[0] == "decrease":
        current_array = [int(x) for x in current_array]
        current_array = [x-1 for x in current_array]


print(*current_array, sep=", ")
