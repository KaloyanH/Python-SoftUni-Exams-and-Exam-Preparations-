from collections import deque

elf_energy = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]

toys = 0
total_energy = 0
current_elf = 0

while elf_energy and materials:

    not_energy = False

    if elf_energy[0] < 5:
        elf_energy.popleft()
        continue
    current_elf += 1

    if current_elf % 3 == 0:
        if elf_energy[0] >= materials[-1] * 2:
            toys += 2
            total_energy += materials[-1] * 2
            elf_energy[0] -= materials[-1] * 2
            materials.pop()
            elf_energy.append(elf_energy.popleft() + 1)
        else:
            not_energy = True

    elif current_elf % 5 == 0:
        if elf_energy[0] >= materials[-1]:
            total_energy += materials[-1]
            elf_energy[0] -= materials[-1]
            if current_elf % 3 == 0:
                if elf_energy[0] >= materials[-1] * 2:
                    elf_energy[0] -= materials[-1] * 2
                if len(materials) > 1:
                    materials.pop()
            materials.pop()
            elf_energy.append(elf_energy.popleft())
        else:
            not_energy = True

    elif elf_energy[0] >= materials[-1]:
        toys += 1
        total_energy += materials[-1]
        elf_energy[0] -= materials[-1]
        materials.pop()
        elf_energy.append(elf_energy.popleft() + 1)

    else:
        not_energy = True

    if not_energy:
        elf_energy[0] *= 2
        elf_energy.append(elf_energy.popleft())

print(f"Toys: {toys}")
print(f"Energy: {total_energy}")

if elf_energy:
    print(f"Elves left: {', '.join(str(x) for x in elf_energy)}")

if materials:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")
