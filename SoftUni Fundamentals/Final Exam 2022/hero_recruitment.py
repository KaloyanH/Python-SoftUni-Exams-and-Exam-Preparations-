

heroes_collection = {}

while True:

    command = input().split()

    if command[0] == "End":
        break

    elif command[0] == "Enroll":
        hero_name = command[1]
        if hero_name in heroes_collection:
            print(f"{hero_name} is already enrolled.")
        else:
            heroes_collection[hero_name] = []

    elif command[0] == "Learn":
        hero_name = command[1]
        spell_name = command[2]
        if hero_name not in heroes_collection:
            print(f"{hero_name} doesn't exist.")
            continue
        if spell_name in heroes_collection[hero_name]:
            print(f'{hero_name} has already learnt {spell_name}.')
            continue
        else:
            heroes_collection[hero_name].append(spell_name)

    elif command[0] == "Unlearn":
        hero_name = command[1]
        spells_name = command[2]
        if hero_name not in heroes_collection:
            print(f"{hero_name} doesn't exist.")
            continue
        if spells_name not in heroes_collection[hero_name]:
            print(f"{hero_name} doesn't know {spells_name}.")
            continue
        else:
            heroes_collection[hero_name].remove(spells_name)
print("Heroes:")
for name in heroes_collection.items():
    if len(name[1]) > 0:
        hero_name = name[0]
        list_of_spells = ", ".join(name[1])
        print(f"== {hero_name}: {list_of_spells}")
    else:
        hero_name = name[0]
        print(f"== {hero_name}:")
