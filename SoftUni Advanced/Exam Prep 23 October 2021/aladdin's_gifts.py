from collections import deque

materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])

gifts = {

    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0,

}

while materials and magic_level:

    magic_needed = materials[-1] + magic_level[0]

    if magic_needed < 100:
        if magic_needed % 2 == 0:
            magic_needed = materials[-1] * 2 + magic_level[0] * 3
            if not 100 <= magic_needed <= 499:
                materials.pop()
                magic_level.popleft()
                continue

        elif magic_needed % 2 != 0:
            magic_needed = (materials[-1] + magic_level[0]) * 2
            if not 100 <= magic_needed <= 499:
                materials.pop()
                magic_level.popleft()
                continue

    if magic_needed > 499:
        magic_needed /= 2
        if not 100 <= magic_needed <= 499:
            materials.pop()
            magic_level.popleft()
            continue

    if 100 <= magic_needed <= 199:
        gifts["Gemstone"] += 1
        materials.pop()
        magic_level.popleft()

    elif 200 <= magic_needed <= 299:
        gifts["Porcelain Sculpture"] += 1
        materials.pop()
        magic_level.popleft()

    elif 300 <= magic_needed <= 399:
        gifts["Gold"] += 1
        materials.pop()
        magic_level.popleft()

    elif 400 <= magic_needed <= 499:
        gifts["Diamond Jewellery"] += 1
        materials.pop()
        magic_level.popleft()

if gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"] > 0 or gifts["Gold"] > 0 and gifts["Diamond Jewellery"] > 0:
    print(f"The wedding presents are made!")
else:
    print(f"Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")

if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for key, value in gifts.items():
    if value > 0:
        print(f"{key}: {value}")
