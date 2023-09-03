rooms = input().split("|")

initial_health = 100
bitcoins = 0
room_counter = 0
win_condition = True

for room in rooms:

    current_room = room.split()
    first_cmd = current_room[0]
    second_cmd = int(current_room[1])
    room_counter += 1
    if first_cmd == "potion":
        temp_health = initial_health
        initial_health += second_cmd
        if initial_health > 100:
            initial_health = 100
        gained_health = initial_health - temp_health
        print(f"You healed for {gained_health} hp.")
        print(f"Current health: {initial_health} hp.")

    elif first_cmd == "chest":
        bitcoins += second_cmd
        print(f"You found {second_cmd} bitcoins.")

    else:
        monster = first_cmd
        attack = second_cmd
        initial_health -= attack

        if initial_health > 0:
            print(f"You slayed {monster}.")

        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {room_counter}")
            win_condition = False
            break

if win_condition:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {initial_health}")

