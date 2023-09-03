def drive_funct(cars_collection, current_cmd):
    car = current_cmd[1]
    distance = int(current_cmd[2])
    fuel = int(current_cmd[3])

    if fuel > cars_collection[car]["fuel"]:
        print(f"Not enough fuel to make that ride")

    else:
        cars_collection[car]["mileage"] += distance
        cars_collection[car]["fuel"] -= fuel
        print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

    if cars_collection[car]["mileage"] >= 100000:
        print(f"Time to sell the {car}!")
        cars_collection.pop(car)


    return cars_collection


def refuel_funct(cars_collection, current_cmd):
    car = current_cmd[1]
    fuel = int(current_cmd[2])

    cars_collection[car]["fuel"] += fuel
    if cars_collection[car]["fuel"] > 75:
        leftover_fuel = cars_collection[car]["fuel"] - 75
        required_fuel = fuel - leftover_fuel
        print(f"{car} refueled with {required_fuel} liters")
        cars_collection[car]["fuel"] = 75
        return cars_collection
    print(f"{car} refueled with {fuel} liters")
    return cars_collection


def revert_funct(cars_collection, current_cmd):
    car = current_cmd[1]
    kilometers = int(current_cmd[2])

    cars_collection[car]["mileage"] -= kilometers

    if cars_collection[car]["mileage"] < 10000:
        cars_collection[car]["mileage"] = 10000
        return cars_collection

    else:
        print(f"{car} mileage decreased by {kilometers} kilometers")
        return cars_collection


number_of_cars = int(input())

cars_collection = {}

for _ in range(number_of_cars):

    current_car = input().split("|")
    car = current_car[0]
    miles = int(current_car[1])
    fuel = int(current_car[2])

    cars_collection[car] = {"mileage": miles, "fuel": fuel}


while True:

    current_cmd = input().split(" : ")

    if current_cmd[0] == "Stop":
        break

    elif current_cmd[0] == "Drive":
        drive_funct(cars_collection, current_cmd)

    elif current_cmd[0] == "Refuel":
        refuel_funct(cars_collection, current_cmd)

    elif current_cmd[0] == "Revert":
        revert_funct(cars_collection, current_cmd)


for car in cars_collection.items():
    mileage = list(car[1].values())[0]
    fuel = list(car[1].values())[1]

    print(f"{car[0]} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")

