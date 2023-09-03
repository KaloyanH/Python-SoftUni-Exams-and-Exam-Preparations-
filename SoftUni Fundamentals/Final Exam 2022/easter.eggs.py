import re

some_string = input()

eastern_pattern = r"[\#|\@]+(?P<color>[a-z]{3,})[\#|\@]+[^a-z0-9]*[\/]+(?P<number>[\d]+)[\/]+"

eastern_eggs = re.finditer(eastern_pattern, some_string)

for eggs in eastern_eggs:
    print(f"You found {eggs['number']} {eggs['color']} eggs!")
