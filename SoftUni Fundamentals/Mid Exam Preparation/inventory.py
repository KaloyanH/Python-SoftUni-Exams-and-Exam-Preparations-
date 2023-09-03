journal = input().split(", ")


while True:

    command = input().split(" - ")

    if command[0] == "Craft!":
        break

    if command[0] == "Collect":
        item = command[1]
        if item in journal:
            continue
        else:
            journal.append(item)

    elif command[0] == "Drop":
        item = command[1]
        if item in journal:
            journal.remove(item)

    elif command[0] == "Combine Items":
        current_items = command[1].split(":")
        old_item = current_items[0]
        new_item = current_items[1]
        if old_item in journal:
            old_item_index = journal.index(old_item)
            journal.insert(old_item_index + 1, new_item)

    elif command[0] == "Renew":
        item = command[1]
        if item in journal:
            journal.remove(item)
            journal.append(item)

print(", ".join(journal))
