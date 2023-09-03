food = float(input())
hay = float(input())
cover = float(input())
weight = float(input())

have_commodities = True

food_gr = food * 1000
hay_gr = hay * 1000
cover_gr = cover * 1000
weight_gr = weight * 1000


for days in range(1, 31):
    food_gr -= 300

    if days % 2 == 0:
        hay_gr -= food_gr * 0.05

    if days % 3 == 0:
        cover_gr -= weight_gr * 0.333

    if food_gr <= 0:
        have_commodities = False
        break
    elif hay_gr <= 0:
        have_commodities = False
        break
    elif cover_gr <= 0:
        have_commodities = False
        break

if have_commodities:
    print(f"Everything is fine! Puppy is happy! Food: {(food_gr/1000):.2f}, Hay: {(hay_gr/1000):.2f}, Cover: {(cover_gr/1000):.2f}.")

else:
    print("Merry must go to the pet store!")
