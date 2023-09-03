encrypted_msg = input()

while True:

    command = input().split("|")

    if command[0] == "Decode":
        break

    if command[0] == "Move":
        letters = int(command[1])
        encrypted_msg = encrypted_msg[letters:] + encrypted_msg[:letters]

    elif command[0] == "Insert":
        idx = int(command[1])
        value = command[2]
        encrypted_msg = encrypted_msg[:idx] + value + encrypted_msg[idx:]

    elif command[0] == "ChangeAll":
        substring = command[1]
        replace = command[2]
        encrypted_msg = encrypted_msg.replace(substring, replace)

print(f"The decrypted message is: {encrypted_msg}")
