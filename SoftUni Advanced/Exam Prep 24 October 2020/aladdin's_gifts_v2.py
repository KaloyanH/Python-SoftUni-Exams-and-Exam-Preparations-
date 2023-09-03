from collections import deque


def crafting_gifts(total_sum, mats, magic, gifts_dict):

    if total_sum in range(100, 200):
        gifts_dict["Gemstone"] += 1
    elif total_sum in range(200, 300):
        gifts_dict["Porcelain Sculpture"] += 1
    elif total_sum in range(300, 400):
        gifts_dict["Gold"] += 1
    elif total_sum in range(400, 500):
        gifts_dict["Diamond Jewellery"] += 1
    mats.pop()
    magic.popleft()
    return gifts_dict


materials = [int(x) for x in input().split()]
magic_level = deque([int(x) for x in input().split()])


gifts_dict = {

    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0

}


while materials and magic_level:

    total_sum = materials[-1] + magic_level[0]

    if 100 <= total_sum <= 499:
        crafting_gifts(total_sum, materials, magic_level, gifts_dict)

    elif total_sum < 100:
        if total_sum % 2 == 0:
            total_sum = materials[-1] * 2 + magic_level[0] * 3
            crafting_gifts(total_sum, materials, magic_level, gifts_dict)
        elif total_sum % 2 != 0:
            total_sum *= 2
            crafting_gifts(total_sum, materials, magic_level, gifts_dict)

    elif total_sum > 499:
        total_sum //= 2
        crafting_gifts(total_sum, materials, magic_level, gifts_dict)

if gifts_dict["Gemstone"] > 0 and gifts_dict["Porcelain Sculpture"] > 0 or \
        gifts_dict["Gold"] > 0 and gifts_dict["Diamond Jewellery"] > 0:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_level:
    print(f"Magic left: {', '.join(str(x) for x in magic_level)}")

for key, value in sorted(gifts_dict.items()):
    if value > 0:
        print(f"{key}: {value}")



