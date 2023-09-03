def numbers_func(num):
    average_sum = sum(num) / len(num)
    numbers_above_average = [numbers for numbers in num if numbers > average_sum]
    needed_numbers = []

    if numbers_above_average:

        for numbers in sorted(numbers_above_average)[::-1]:
            if len(needed_numbers) < 5:
                needed_numbers.append(numbers)
    else:
        print("No")

    return " ".join(str(num) for num in needed_numbers)


number = list(map(int, input().split()))
print(numbers_func(number))
