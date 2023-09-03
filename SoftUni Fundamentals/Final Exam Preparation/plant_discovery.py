from collections import defaultdict

number = int(input())
plants = defaultdict(dict)

for _ in range(number):
    plant_data = input().split("<->")
    plant = plant_data[0]
    rarity = float(plant_data[1])
    if plant not in plants:
        plants[plant] = {"Rarity": rarity, "Rating": []}
    else:
        plants[plant]["Rarity"] += rarity

while True:
    command = input()
    if command == "Exhibition":
        break
    command_data = command.split(":")
    command_type = command_data[0]
    if command_type == "Rate":
        data = command_data[1]
        data = data.split(" - ")
        plant_name = data[0].strip()
        rating = float(data[1])
        if plant_name in plants:
            plants[plant_name]["Rating"].append(rating)
        else:
            print("error")
    elif command_type == "Update":
        data = command_data[1]
        data = data.split(" - ")
        plant_name = data[0].strip()
        new_rarity = float(data[1])
        if plant_name in plants:
            plants[plant_name]["Rarity"] = new_rarity
        else:
            print("error")
    elif command_type == "Reset":
        plant_name = command_data[1].strip()
        if plant_name in plants:
            plants[plant_name]["Rating"] = []
        else:
            print("error")

print("Plants for the exhibition:")
for plant in plants.items():
    rarity = list(plant[1].values())[0]
    rating = list(plant[1].values())[1]

    if rating and rarity:
        average_rating = sum(rating) / len(rating)
    else:
        average_rating = 0

    print(f"- {plant[0]}; Rarity: {int(rarity)}; Rating: {average_rating:.2f}")
