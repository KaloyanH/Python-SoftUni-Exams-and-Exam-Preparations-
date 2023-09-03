from collections import deque

mg_of_caffeine = [int(x) for x in input().split(", ")]
nrg_drinks = deque([int(x) for x in input().split(", ")])

total_caffeine = 0
coffeine_permitted = 300

while mg_of_caffeine and nrg_drinks:

    caffeine_per_night = mg_of_caffeine[-1] * nrg_drinks[0]


    if caffeine_per_night <= coffeine_permitted:
        total_caffeine += caffeine_per_night
        coffeine_permitted -= caffeine_per_night
        mg_of_caffeine.pop()
        nrg_drinks.popleft()

    else:
        mg_of_caffeine.pop()
        nrg_drinks.append(nrg_drinks.popleft())
        total_caffeine -= 30
        if total_caffeine > 0:
            coffeine_permitted += 30
        if total_caffeine < 0:
            total_caffeine = 0





if nrg_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in nrg_drinks)}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")
