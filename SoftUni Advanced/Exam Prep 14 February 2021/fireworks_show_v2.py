from collections import deque

firework_effect = deque([int(x) for x in input().split(", ")])
explosive_power = [int(x) for x in input().split(", ")]

fireworks = {

    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0

}

fireworks_gathered = False

while firework_effect and explosive_power:

    below_zero = False

    if firework_effect[0] <= 0:
        firework_effect.popleft()
        below_zero = True

    if explosive_power[-1] <= 0:
        explosive_power.pop()
        below_zero = True

    if below_zero:
        continue

    current_sum = firework_effect[0] + explosive_power[-1]

    if current_sum % 15 == 0:
        fireworks["Crossette Fireworks"] += 1
        firework_effect.popleft()
        explosive_power.pop()

    elif current_sum % 3 == 0:
        fireworks["Palm Fireworks"] += 1
        firework_effect.popleft()
        explosive_power.pop()

    elif current_sum % 5 == 0:
        fireworks["Willow Fireworks"] += 1
        firework_effect.popleft()
        explosive_power.pop()

    else:
        firework_effect.append(firework_effect.popleft() - 1)

    if all(int(x) >= 3 for x in fireworks.values()):
        fireworks_gathered = True
        break

if fireworks_gathered:
    print(f"Congrats! You made the perfect firework show!")
else:
    print(f"Sorry. You can't make the perfect firework show.")
if firework_effect:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effect)}")
if explosive_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_power)}")

for key, value in fireworks.items():
    print(f"{key}: {value}")
