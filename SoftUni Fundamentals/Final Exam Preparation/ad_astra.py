import re


text = input()

expression = r"([|#])(?P<product>[A-Za-z\s]+)\1(?P<expiration>\d{2}/\d{2}/\d{2})\1(?P<calories>\d{1,5})\1"

matches = re.finditer(expression, text)

total_calories = 0

for match in matches:
    total_calories += int(match.group("calories"))

days_to_survive = total_calories // 2000

print(f"You have food to last you for: {days_to_survive} days!")

expression = r"([|#])(?P<product>[A-Za-z\s]+)\1(?P<expiration>\d{2}/\d{2}/\d{2})\1(?P<calories>\d{1,5})\1"

matches = re.finditer(expression, text)

for match in matches:
    item = match.group("product")
    best_before = match.group("expiration")
    nutrition = match.group("calories")
    print(f"Item: {item}, Best before: {best_before}, Nutrition: {nutrition}")


