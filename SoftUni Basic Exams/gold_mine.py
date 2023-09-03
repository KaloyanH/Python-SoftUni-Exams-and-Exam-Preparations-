count_locations = int(input())

for runs in range(count_locations):
    expected_debit = float(input())
    number_of_days = int(input())

    total_gold_per_day = 0
    average_gold_per_day = 0

    for debit in range(number_of_days):
        gold_per_day = float(input())
        total_gold_per_day += gold_per_day
        average_gold_per_day = total_gold_per_day / number_of_days

    if average_gold_per_day >= expected_debit:
        print(f"Good job! Average gold per day: {average_gold_per_day:.2f}.")

    else:
        print(f"You need {(abs(average_gold_per_day - expected_debit)):.2f} gold.")

