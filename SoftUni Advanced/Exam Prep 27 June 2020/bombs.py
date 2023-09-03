from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]

bombs_dict = {

    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs"

}

bombs_made = {"Cherry Bombs": 0, "Datura Bombs": 0, "Smoke Decoy Bombs": 0}
bombs_completed = False

while bomb_casings and bomb_effects:

    if all(x >= 3 for x in bombs_made.values()):
        bombs_completed = True
        break

    current_effect = bomb_effects.popleft()
    current_casing = bomb_casings.pop()

    result = current_effect + current_casing

    if result in bombs_dict:
        bomb = bombs_dict[result]
        if bomb in bombs_made:
            bombs_made[bomb] += 1
        else:
            bombs_made[bomb] = 1

    else:
        bomb_effects.appendleft(current_effect)
        bomb_casings.append(current_casing - 5)

if bombs_completed:
    print(f"Bene! You have successfully filled the bomb pouch!")
else:
    print(f"You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print(f"Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")

if not bomb_casings:
    print(f"Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")

result = {}

for key, value in sorted(bombs_made.items()):
    print(f"{key}: {value}")
