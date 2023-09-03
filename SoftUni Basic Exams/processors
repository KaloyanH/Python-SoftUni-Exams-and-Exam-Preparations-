
import math

number_cpus = int(input())
number_workers = int(input())
working_days = int(input())

total_hours = number_workers * working_days * 8
total_cpus = math.floor(total_hours / 3)

difference = abs(number_cpus - total_cpus)

if number_cpus <= total_cpus:
    print(f"Profit: -> {(difference * 110.10):.2f} BGN")
else:
    print(f"Losses: -> {(difference * 110.10):.2f} BGN")
