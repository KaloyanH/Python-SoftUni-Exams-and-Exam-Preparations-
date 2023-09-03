def plunder_funct(cities_dict, current_event):
    city = current_event[1]
    populus = int(current_event[2])
    gold = int(current_event[3])

    cities_dict[city]["pop"] -= populus
    cities_dict[city]["gold"] -= gold

    print(f"{city} plundered! {gold} gold stolen, {populus} citizens killed.")

    if cities_dict[city]["pop"] <= 0 or cities_dict[city]["gold"] <=0:
        cities_dict.pop(city)
        print(f"{city} has been wiped off the map!")


def prosper_funct(cities_dict, current_event):
    city =current_event[1]
    gold = int(current_event[2])

    if gold < 0:
        print("Gold added cannot be a negative number!")
        return cities_dict
    else:
        cities_dict[city]["gold"] += gold
        print(f"{gold} gold added to the city treasury. {city} now has {cities_dict[city]['gold']} gold.")
        return cities_dict


command = input()

cities_dict = {}

while True:

    current_cmd = command.split("||")

    if current_cmd[0] == "Sail":
        break

    city = current_cmd[0]
    populus = int(current_cmd[1])
    gold = int(current_cmd[2])

    if city in cities_dict:
        cities_dict[city]["pop"] += populus
        cities_dict[city]["gold"] += gold

    else:
        cities_dict[city] = {"pop": populus, "gold": gold}

    command = input()


while True:

    current_event = input().split("=>")

    if current_event[0] == "End":
        break

    elif current_event[0] == "Plunder":
        plunder_funct(cities_dict, current_event)

    elif current_event[0] == "Prosper":
        prosper_funct(cities_dict, current_event)


if not cities_dict:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")

else:
    print(f"Ahoy, Captain! There are {len(cities_dict)} wealthy settlements to go to:")
    for city in cities_dict.items():
        people = list(city[1].values())[0]
        gold = list(city[1].values())[1]

        print(f"{city[0]} -> Population: {people} citizens, Gold: {gold} kg")
