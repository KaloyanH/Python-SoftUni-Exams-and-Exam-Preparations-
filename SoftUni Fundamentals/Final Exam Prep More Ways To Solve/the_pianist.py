def add_funct(current_cmd, pieces_dict):
    piece , composer , key = current_cmd[1], current_cmd[2], current_cmd[3]
    if piece in pieces_dict:
        print(f"{piece} is already in the collection!")
        return pieces_dict
    pieces_dict[piece] = {"composer": composer, "key": key}
    print(f"{piece} by {composer} in {key} added to the collection!")
    return pieces_dict


def remove_funct(current_cmd, pieces_dict):
    piece = current_cmd[1]
    if piece in pieces_dict:
       pieces_dict.pop(piece)
       print(f"Successfully removed {piece}!")
       return pieces_dict
    print(f"Invalid operation! {piece} does not exist in the collection.")
    return pieces_dict


def changekey_funct(current_cmd, pieces_dict):
    piece , new_key = current_cmd[1], current_cmd[2]
    if piece in pieces_dict:
        pieces_dict[piece]["key"] = new_key
        print(f"Changed the key of {piece} to {new_key}!")
        return pieces_dict
    print(f"Invalid operation! {piece} does not exist in the collection.")
    return pieces_dict


pieces = int(input())

pieces_dict = {}

for _ in range(pieces):
    piece, composer, key = input().split("|")
    pieces_dict[piece] = {"composer": composer, "key": key}

while True:
    current_cmd = input().split("|")

    if current_cmd[0] == "Stop":
        break

    elif current_cmd[0] == "Add":
        add_funct(current_cmd, pieces_dict)

    elif current_cmd[0] == "Remove":
        remove_funct(current_cmd, pieces_dict)

    elif current_cmd[0] == "ChangeKey":
        changekey_funct(current_cmd, pieces_dict)

for musical_pieces in pieces_dict.items():
    print(f"{musical_pieces[0]} -> Composer: {list(musical_pieces[1].values())[0]}, Key: {list(musical_pieces[1].values())[1]}")
