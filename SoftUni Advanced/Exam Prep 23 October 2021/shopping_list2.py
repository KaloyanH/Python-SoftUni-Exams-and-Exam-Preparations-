def shopping_list(*args, **kwargs):
    result = ""
    budget = args[0]
    products = 0

    if budget < 100:
        return "You do not have enough budget."

    for item, values in kwargs.items():

        if products == 5:
            break
        price, quantity = values
        total_sum = price * quantity

        if budget >= total_sum:
            budget -= total_sum
            result += f"You bought {item} for {total_sum:.2f} leva.""\n"
            products += 1

    return result



print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))