import re

text_string = input()

pattern = r"([#|\\])(?P<products>[A-Za-z\s]+)(\1)(?P<date>\d{2}/\d{2}/\d{2})(\1)(?P<calories>\d+)(\1)"

searched_items = re.finditer(pattern, text_string)

total_cals = 0

for item in searched_items:
    calories = int(item.group("calories"))
    total_cals += calories

days_to_survive = total_cals // 2000

print(f"You have food to last you for: {days_to_survive} days!")

pattern = r"([#|\\])(?P<products>[A-Za-z\s]+)(\1)(?P<date>\d{2}/\d{2}/\d{2})(\1)(?P<calories>\d+)(\1)"

searched_items = re.finditer(pattern, text_string)


for item in searched_items:
    product = item.group("products")
    date = item.group("date")
    calories = item.group("calories")
    print(f"Item: {product}, Best before: {date}, Nutrition: {calories}")



