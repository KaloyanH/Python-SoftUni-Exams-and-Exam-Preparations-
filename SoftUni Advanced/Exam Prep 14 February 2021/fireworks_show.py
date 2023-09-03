from collections import deque

firework_effects = deque([int(x) for x in input().split(", ")])
explosive_power = ([int(x) for x in input().split(", ")])

fireworks = {

    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0,

}

fireworks_completed = False
invalid_number = False

while firework_effects and explosive_power:

    invalid_number = False

    if all(x >= 3 for x in fireworks.values()):
        fireworks_completed = True
        break

    if firework_effects[0] <= 0:
        firework_effects.pop()
        invalid_number = True

    if explosive_power[-1] <= 0:
        explosive_power.pop()
        invalid_number = True

    if invalid_number:
        continue

    sum_of_values = firework_effects[0] + explosive_power[-1]

    if sum_of_values % 3 == 0 and sum_of_values % 5 != 0:
        fireworks["Palm Fireworks"] += 1
        explosive_power.pop()
        firework_effects.popleft()

    elif sum_of_values % 5 == 0 and sum_of_values % 3 != 0:
        fireworks["Willow Fireworks"] += 1
        explosive_power.pop()
        firework_effects.popleft()

    elif sum_of_values % 3 == 0 and sum_of_values % 5 == 0:
        fireworks["Crossette Fireworks"] += 1
        explosive_power.pop()
        firework_effects.popleft()
    else:
        firework_effects.append(firework_effects.popleft() - 1)


if all(x >= 3 for x in fireworks.values()):
    fireworks_completed = True

if fireworks_completed:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")
if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

for key, value in fireworks.items():
    print(f"{key}: {value}")
