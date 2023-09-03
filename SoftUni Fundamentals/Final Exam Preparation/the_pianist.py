def add_funct(current_cmd, collection):
    piece = current_cmd[1]
    composer = current_cmd[2]
    key = current_cmd[3]

    if piece in collection:
        print(f"{piece} is already in the collection!")
    else:
        collection[piece] = {"composer": composer, "key": key}
        print(f"{piece} by {composer} in {key} added to the collection!")
    return collection


def remove_funct(current_cmd, collection):
    piece = current_cmd[1]

    if piece in collection:
        collection.pop(piece)
        print(f"Successfully removed {piece}!")
        return collection
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


def change_funct(current_cmd, collection):
    piece = current_cmd[1]
    new_key = current_cmd[2]

    if piece in collection:
        collection[piece]["key"] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
        return collection
    else:
        print(f"Invalid operation! {piece} does not exist in the collection.")


number_of_pieces = int(input())

collection = {}

for _ in range(number_of_pieces):

    pieces = input().split("|")
    piece = pieces[0]
    composer = pieces[1]
    key = pieces[2]
    collection[piece] = {"composer": composer, "key": key}


while True:

    current_cmd = input().split("|")

    if current_cmd[0] == "Stop":
        break

    elif current_cmd[0] == "Add":
        add_funct(current_cmd, collection)

    elif current_cmd[0] == "Remove":
        remove_funct(current_cmd, collection)

    elif current_cmd[0] == "ChangeKey":
        change_funct(current_cmd, collection)


for composers in collection.items():
    composer = list(composers[1].values())[0]
    key = list(composers[1].values())[1]
    print(f"{composers[0]} -> Composer: {composer}, Key: {key}")
