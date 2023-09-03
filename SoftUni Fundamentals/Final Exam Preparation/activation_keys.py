act_key = input()

while True:

    command = input().split(">>>")

    if command[0] == "Generate":
        break

    if command[0] == "Contains":
        substring = command[1]
        if substring in act_key:
            print(f"{act_key} contains {substring}")

        else:
            print("Substring not found!")

    elif command[0] == "Flip":
        new_cmd = command[1].split("/")
        start_index = int(command[2])
        end_index = int(command[3])
        if new_cmd[0] == "Upper":
            act_key = act_key[:start_index] + act_key[start_index:end_index].upper() + act_key[end_index:]

        elif new_cmd[0] == "Lower":
            act_key = act_key[:start_index] + act_key[start_index:end_index].lower() + act_key[end_index:]
        print(act_key)

    elif command[0] == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        act_key = act_key[:start_index] + act_key[end_index:]
        print(act_key)

print(f"Your activation key is: {act_key}")

