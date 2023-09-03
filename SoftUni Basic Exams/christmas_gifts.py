command = input()

number_of_kids = 0
number_of_adults = 0
sum_toys = 0
sum_sweaters = 0

while command != "Christmas":
    age = int(command)
    if age <= 16:
        number_of_kids += 1
        sum_toys += 5
    elif age > 16:
        number_of_adults += 1
        sum_sweaters += 15
    command = input()

print(f"Number of adults: {number_of_adults}")
print(f"Number of kids: {number_of_kids}")
print(f"Money for toys: {sum_toys}")
print(f"Money for sweaters: {sum_sweaters}")
