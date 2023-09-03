def spell_funct(heroes_dict, command):
    hero_name = command[1]
    mp_needed = int(command[2])
    spell_name = command[3]

    if heroes_dict[hero_name]["mp"] >= mp_needed:
        heroes_dict[hero_name]["mp"] -= mp_needed
        print(f"{hero_name} has successfully cast {spell_name} and now has {heroes_dict[hero_name]['mp']} MP!")

    else:
        print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    return heroes_dict


def damage_funct(heroes_dict, command):
    hero_name = command[1]
    dmg_taken = int(command[2])
    attacker = command[3]

    heroes_dict[hero_name]["hp"] -= dmg_taken
    if heroes_dict[hero_name]["hp"] > 0:
        print(
            f"{hero_name} was hit for {dmg_taken} HP by {attacker} and now has {heroes_dict[hero_name]['hp']} HP left!")
    else:
        heroes_dict.pop(hero_name)
        print(f"{hero_name} has been killed by {attacker}!")

    return heroes_dict


def recharge_funct(heroes_dict, command):
    hero_name = command[1]
    amount = int(command[2])

    heroes_dict[hero_name]["mp"] += amount
    if heroes_dict[hero_name]["mp"] > 200:
        leftover_mp = heroes_dict[hero_name]["mp"] - 200
        required_mp = amount - leftover_mp
        print(f"{hero_name} recharged for {required_mp} MP!")
        heroes_dict[hero_name]["mp"] = 200
        return heroes_dict

    else:
        print(f"{hero_name} recharged for {amount} MP!")
        return heroes_dict


def heal_func(heroes_dict, command):
    hero_name = command[1]
    amount = int(command[2])

    heroes_dict[hero_name]["hp"] += amount
    if heroes_dict[hero_name]["hp"] > 100:
        leftover_hp = heroes_dict[hero_name]["hp"] - 100
        required_hp = amount - leftover_hp
        print(f"{hero_name} healed for {required_hp} HP!")
        heroes_dict[hero_name]["hp"] = 100
        return heroes_dict
    else:
        print(f"{hero_name} healed for {amount} HP!")
        return heroes_dict


number_of_heroes = int(input())

heroes_dict = {}

for _ in range(number_of_heroes):
    current_cmd = input().split()
    hero_name = current_cmd[0]
    hit_points = int(current_cmd[1])
    mana_points = int(current_cmd[2])
    heroes_dict[hero_name] = {"hp": hit_points, "mp": mana_points}

while True:
    command = input().split(" - ")

    if command[0] == "End":
        break

    elif command[0] == "CastSpell":
        spell_funct(heroes_dict, command)

    elif command[0] == "TakeDamage":
        damage_funct(heroes_dict, command)

    elif command[0] == "Recharge":
        recharge_funct(heroes_dict, command)

    elif command[0] == "Heal":
        heal_func(heroes_dict, command)

for heroes in heroes_dict.items():
    hp = list(heroes[1].values())[0]
    mp = list(heroes[1].values())[1]

    print(heroes[0])
    print(f"  HP: {hp}")
    print(f"  MP: {mp}")
