given_string = input()

while True:

    current_cmd = input().split()

    if current_cmd[0] == "Done":
        break

    elif current_cmd[0] == "Change":
        current_char = current_cmd[1]
        replace_char = current_cmd[2]
        given_string = given_string.replace(current_char, replace_char)
        print(given_string)

    elif current_cmd[0] == "Includes":
        current_substring = current_cmd[1]
        if current_substring in given_string:
            print("True")
        else:
            print("False")

    elif current_cmd[0] == "End":
        substring = current_cmd[1]
        if given_string.endswith(substring):
            print("True")
        else:
            print("False")

    elif current_cmd[0] == "Uppercase":
        given_string = given_string.upper()
        print(given_string)

    elif current_cmd[0] == "FindIndex":
        current_char = current_cmd[1]
        result = given_string.index(current_char)
        print(result)

    elif current_cmd[0] == "Cut":
        start_idx = int(current_cmd[1])
        end_idx = int(current_cmd[2])
        given_string = given_string[start_idx:start_idx+end_idx]
        print(given_string)
