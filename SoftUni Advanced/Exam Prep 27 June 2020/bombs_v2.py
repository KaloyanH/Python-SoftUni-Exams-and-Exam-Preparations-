from collections import deque

bomb_effects = deque([int(x) for x in input().split(", ")])
bomb_casings = [int(x) for x in input().split(", ")]

bombs_dict = {

    40: "Datura Bombs",
    60: "Cherry Bombs",
    120: "Smoke Decoy Bombs",

}

bombs_made = {"Cherry Bombs": 0, "Datura Bombs": 0, "Smoke Decoy Bombs": 0}

all_bombs = False

while bomb_effects and bomb_casings:

    if all(int(x) >= 3 for x in bombs_made.values()):
        all_bombs = True
        break

    sum_mats = bomb_effects[0] + bomb_casings[-1]

    if sum_mats in bombs_dict:
        bombs_made[bombs_dict[sum_mats]] += 1
        bomb_effects.popleft()
        bomb_casings.pop()
    else:
        bomb_casings[-1] -= 5

if all_bombs:
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

for key, value in sorted(bombs_made.items()):
    print(f"{key}: {value}")
