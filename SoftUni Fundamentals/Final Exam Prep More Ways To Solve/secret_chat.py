def insert_funct(cmd, secret_message):
    index = int(cmd[1])
    secret_message = secret_message[:index] + " " + secret_message[index:]
    print(secret_message)
    return secret_message


def reverse_funct(cmd, secret_message):
    substring = cmd[1]
    if substring in secret_message:
        secret_message = secret_message.replace(substring, "", 1)
        rev_string = substring[::-1]
        secret_message = secret_message + rev_string
        print(secret_message)
        return secret_message
    print("error")
    return secret_message


def change_funct(cmd, secret_message):
    substring, replacement = cmd[1], cmd[2]
    secret_message = secret_message.replace(substring, replacement)
    print(secret_message)
    return secret_message


secret_message = input()

while True:

    cmd = input().split(":|:")

    if cmd[0] == "Reveal":
        break

    elif cmd[0] == "InsertSpace":
        secret_message = insert_funct(cmd, secret_message)

    elif cmd[0] == "Reverse":
        secret_message = reverse_funct(cmd, secret_message)

    elif cmd[0] == "ChangeAll":
        secret_message = change_funct(cmd, secret_message)

print(f"You have a new text message: {secret_message}")
