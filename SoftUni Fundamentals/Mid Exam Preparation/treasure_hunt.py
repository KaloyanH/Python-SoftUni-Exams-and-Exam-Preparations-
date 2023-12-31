main_treasure_check = input().split("|")

command = input()

while command != "Yohoho!":
    command = command.split()
    type_command = command[0]
    if type_command == "Loot":
        for index, item in enumerate(command):
            if index != 0 and item not in main_treasure_check:
                main_treasure_check.insert(0, item)
    elif type_command == "Drop":
        index_item = int(command[-1])
        if abs(index_item) < len(main_treasure_check):
            main_treasure_check.append(main_treasure_check.pop(index_item))
    elif type_command == "Steal":
        count_items = int(command[-1])
        stolen_items = main_treasure_check[-count_items:]
        main_treasure_check = main_treasure_check[:-count_items]
        print(*stolen_items, sep=", ")

    command = input()

if main_treasure_check:
    average_treasure = 0
    for item in main_treasure_check:
        average_treasure += len(item)
    print(f"Average treasure gain: {(average_treasure / len(main_treasure_check)):.2f} pirate credits.")
else:
    print(f"Failed treasure hunt.")
