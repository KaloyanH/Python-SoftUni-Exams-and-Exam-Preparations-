first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
students = int(input())

employees_efficiency_per_hour = first_employee + second_employee + third_employee

time = 0

while students > 0:
    time += 1
    if time % 4 == 0:
        continue
    students -= employees_efficiency_per_hour

print(f"Time needed: {time}h.")
