import re

text = input()

pattern = r"([=|/]{1})([A-Z][A-Za-z]{2,})(\1)"

destinations = re.finditer(pattern, text)

travel_points = 0
all_destinations = []

for match in destinations:
    travel_points += len(match.group(2))
    all_destinations.append(match.group(2))


print(f"Destinations: {', '.join(all_destinations)}")
print(f"Travel Points: {travel_points}")
