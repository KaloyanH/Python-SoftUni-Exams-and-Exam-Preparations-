def rate_funct(cmd, plant_dict):
    plant = cmd[0]
    rating = int(cmd[1])

    if plant in plant_dict:
        plant_dict[plant]["rating"].append(rating)
        return plant_dict
    print("error")


def action_funct(cmd, plant_dict):
    plant = cmd[0]
    rarity = cmd[1]

    if plant in plant_dict:
        plant_dict[plant]["rarity"] = rarity
        return plant_dict
    print("error")


def reset_funct(cmd, plant_dict):
    plant = cmd[0]

    if plant in plant_dict:
        plant_dict[plant]["rating"] = []
        return plant_dict
    print("error")


number_of_lines = int(input())

plant_dict = {}

for _ in range(number_of_lines):
    plant_info = input().split("<->")
    plant = plant_info[0]
    rarity = plant_info[1]

    if plant in plant_dict:
        plant_dict[plant]['rarity'] = rarity
    plant_dict[plant] = {"rarity": rarity, "rating": []}

while True:
    current_cmd = input().split(": ")
    action = current_cmd[0]

    if action == "Exhibition":
        break

    elif action == "Rate":
        cmd = current_cmd[1].split(" - ")
        rate_funct(cmd, plant_dict)

    elif action == "Update":
        cmd = current_cmd[1].split(" - ")
        action_funct(cmd, plant_dict)

    elif action == "Reset":
        cmd = current_cmd[1].split(" - ")
        reset_funct(cmd, plant_dict)

print("Plants for the exhibition:")

for plant in plant_dict.items():
    rarity = list(plant[1].values())[0]
    rating = list(plant[1].values())[1]

    if rating and rarity:
        average_rating = sum(rating) / len(rating)
    else:
        average_rating = 0

    print(f"- {plant[0]}; Rarity: {int(rarity)}; Rating: {average_rating:.2f}")
