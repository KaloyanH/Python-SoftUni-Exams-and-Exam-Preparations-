stops = input()

cmd = input()

while cmd != "Travel":

    current_cmd = cmd.split(":")
    if current_cmd[0] == "Add Stop":
        if 0 <= int(current_cmd[1]) < len(stops):
            index = int(current_cmd[1])
            string = current_cmd[2]
            stops = stops[:index] + string + stops[index:]
        print(stops)

    elif current_cmd[0] == "Remove Stop":
        if 0 <= int(current_cmd[1]) < len(stops) and 0 <= int(current_cmd[2]) < len(stops):
            start_index = int(current_cmd[1])
            end_index = int(current_cmd[2])
            stops = stops[:start_index] + stops[end_index + 1:]
        print(stops)

    elif current_cmd[0] == "Switch":
        old_string = current_cmd[1]
        new_string = current_cmd[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)

    cmd = input()

print(f"Ready for world tour! Planned stops: {stops}")
