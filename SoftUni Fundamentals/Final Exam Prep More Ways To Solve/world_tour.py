def add_funct(command, destination):
    idx = int(command[1])
    string = command[2]
    if 0 <= idx < len(destination):
        destination = destination[:idx] + string + destination[idx:]
    return destination


def remove_funct(command, destination):
    start_idx = int(command[1])
    end_idx = int(command[2])
    if 0 <= start_idx < len(destination) and 0 <= end_idx < len(destination):
        remove_string = destination[start_idx:end_idx + 1]
        destination = destination.replace(remove_string, "")
    return destination


def switch_funct(command, destination):
    old_string = command[1]
    new_string = command[2]
    if old_string in destination:
        destination = destination.replace(old_string, new_string)
    return destination


destination = input()


while True:

    command = input().split(":")

    if command[0] == "Travel":
        break

    elif command[0] == "Add Stop":
        destination = add_funct(command, destination)

    elif command[0] == "Remove Stop":
        destination = remove_funct(command, destination)

    elif command[0] == "Switch":
        destination = switch_funct(command, destination)
    print(destination)

print(f"Ready for world tour! Planned stops: {destination}")
