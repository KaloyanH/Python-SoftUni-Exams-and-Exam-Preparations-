vehicles = input().split(">>")

list_of_cars = ["family", "heavyDuty", "sports"]

total_taxes = 0

for car in vehicles:

    current_car = car.split()
    car_type = current_car[0]
    years = int(current_car[1])
    kilometers = int(current_car[2])

    if car_type not in list_of_cars:
        print("Invalid car type.")
        continue

    if car_type == "family":
        initial_tax = 50
        initial_tax -= years * 5
        initial_tax += + (kilometers // 3000) * 12
        print(f"A {car_type} car will pay {initial_tax:.2f} euros in taxes.")
        total_taxes += initial_tax

    elif car_type == "heavyDuty":
        initial_tax = 80
        initial_tax -= years * 8
        initial_tax += (kilometers // 9000) * 14
        print(f"A {car_type} car will pay {initial_tax:.2f} euros in taxes.")
        total_taxes += initial_tax

    elif car_type == "sports":
        initial_tax = 100
        initial_tax -= years * 9
        initial_tax += (kilometers // 2000) * 18
        print(f"A {car_type} car will pay {initial_tax:.2f} euros in taxes.")
        total_taxes += initial_tax

print(f"The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.")
