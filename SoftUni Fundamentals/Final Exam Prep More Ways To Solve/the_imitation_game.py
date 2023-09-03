def move_funct(cmd, encrypted_msg):
    letters = int(cmd[1])
    encrypted_msg = encrypted_msg[letters:] + encrypted_msg[:letters]
    return encrypted_msg


def insert_funct(cmd, encrypted_msg):
    idx = int(cmd[1])
    value = cmd[2]
    encrypted_msg = encrypted_msg[:idx] + value + encrypted_msg[idx:]
    return encrypted_msg


def change_funct(cmd, encrypted_msg):
    substring = cmd[1]
    replacement = cmd[2]
    if substring in encrypted_msg:
        encrypted_msg = encrypted_msg.replace(substring, replacement)
    return encrypted_msg


encrypted_msg = input()

while True:

    cmd = input().split("|")

    if cmd[0] == "Decode":
        break

    elif cmd[0] == "Move":
        encrypted_msg = move_funct(cmd, encrypted_msg)

    elif cmd[0] == "Insert":
        encrypted_msg = insert_funct(cmd, encrypted_msg)

    elif cmd[0] == "ChangeAll":
        encrypted_msg = change_funct(cmd, encrypted_msg)

print(f"The decrypted message is: {encrypted_msg}")
