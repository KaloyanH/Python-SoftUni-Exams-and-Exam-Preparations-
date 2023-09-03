import re

destinations = input()

valid_destination = r"=[A-Z][a-zA-Z]{2,}=|\/[A-Z][a-zA-Z]{2,}\/"

valid = re.findall(valid_destination, destinations)

length = 0

result = []

for destination in valid:
    destination = destination[1:-1]
    length += len(destination)
    result.append(destination)

print(f"Destinations: {', '.join(result)}")
print(f"Travel Points: {length}")
