price_per_page = float(input())
price_per_cover = float(input())
discount_percent = int(input())
designer_salary = float(input())
percent_team = int(input())


sum_pages = price_per_page * 899
sum_covers = price_per_cover * 2

total_sum_printing = sum_pages + sum_covers

sum_after_discount = total_sum_printing - (total_sum_printing * discount_percent / 100)

total_costs = sum_after_discount + designer_salary

total_sum = total_costs - (total_costs * percent_team / 100)

print(f" Avtonom should pay {total_sum:.2f} BGN.")
