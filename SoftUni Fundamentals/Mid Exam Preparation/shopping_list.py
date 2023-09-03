shopping_list = input().split("!")

while True:
    command = input()

    if command == "Go Shopping!":
        break

    current_command = command.split()

    if current_command[0] == "Urgent":
        item = current_command[1]
        if item in shopping_list:
            continue
        else:
            shopping_list.insert(0, item)

    elif current_command[0] == "Unnecessary":
        item = current_command[1]
        if item in shopping_list:
            shopping_list.remove(item)
        else:
            continue

    elif current_command[0] == "Correct":
        old_item = current_command[1]
        new_item = current_command[2]
        if old_item in shopping_list:
            for i in range(len(shopping_list)):
                if shopping_list[i] == old_item:
                    shopping_list[i] = new_item

        else:
            continue

    elif current_command[0] == "Rearrange":
        item_to_remove = current_command[1]
        if item_to_remove in shopping_list:
            shopping_list.remove(item_to_remove)
            shopping_list.append(item_to_remove)
        else:
            continue

print(", ".join(shopping_list))
