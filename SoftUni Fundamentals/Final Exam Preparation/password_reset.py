password = input()

while True:

    cmd = input()

    current_cmd = cmd.split()

    if current_cmd[0] == "Done":
        break

    if current_cmd[0] == "TakeOdd":
        password = password[1::2]
        print(password)

    elif current_cmd[0] == "Cut":
        idx = int(current_cmd[1])
        length = int(current_cmd[2])
        new_idx = idx + length
        substring = password[idx:new_idx]
        password = password.replace(substring, "", 1)
        print(password)

    elif current_cmd[0] == "Substitute":
        substring = current_cmd[1]
        substitute = current_cmd[2]
        if substring not in password:
            print("Nothing to replace!")
        else:
            password = password.replace(substring, substitute)
            print(password)

print(f"Your password is: {password}")
