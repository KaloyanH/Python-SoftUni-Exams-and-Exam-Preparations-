pirate_ship = list(map(int, input().split(">")))
war_ship = list(map(int, input().split(">")))
maximum_health = int(input())
game_over = False

while True:
    command = input()

    command = command.split()

    if command[0] == "Retire":
        break

    if command[0] == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if 0 <= index < len(war_ship):
            war_ship[index] -= damage
            if war_ship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                game_over = True
                break
        if game_over:
            break

    if command[0] == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            pirate_ship[start_index: end_index + 1] = [i - damage for i in pirate_ship[start_index: end_index +1]]
            for i in pirate_ship:
                if i <= 0:
                    print("You lost! The pirate ship has sunken.")
                    game_over = True
                    break
            if game_over:
                break
        if game_over:
            break

    if command[0] == "Repair":
        index = int(command[1])
        health = int(command[2])
        if 0 <= index < len(pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > maximum_health:
                pirate_ship[index] = maximum_health

    if command[0] == "Status":
        parts_for_repair = []
        minimum_health = maximum_health * 0.2
        for value in pirate_ship:
            if value < minimum_health:
                parts_for_repair.append(value)
        if len(parts_for_repair) > 0:
            print(f"{len(parts_for_repair)} sections need repair.")
        else:
            print("0 sections need repair.")

    if game_over:
        break

if not game_over:
    print(f"Pirate ship status: {sum(pirate_ship)}")
    print(f"Warship status: {sum(war_ship)}")
