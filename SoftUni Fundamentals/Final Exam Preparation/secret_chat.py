string = input()


while True:

    message = input()

    msg = message.split(":|:")

    if msg[0] == "Reveal":
        break

    if msg[0] == "InsertSpace":
        idx = int(msg[1])
        string = string[:idx] + " " + string[idx:]
        print(string)

    elif msg[0] == "Reverse":
        substring = msg[1]
        if substring not in string:
            print("error")
        else:
            new_msg = string.replace(substring, "", 1)
            new_msg = new_msg + substring[::-1]
            string = new_msg
            print(string)

    elif msg[0] == "ChangeAll":
        substring = msg[1]
        replacement = msg[2]
        string = string.replace(substring, replacement)
        print(string)

print(f"You have a new text message: {string}")
