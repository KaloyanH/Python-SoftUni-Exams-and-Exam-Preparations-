def shopping_list(*args, **kwargs):

    result = ""

    budget = args[0]
    counter = 0
    if args[0] < 100:
        return "You do not have enough budget."

    for name, value in kwargs.items():
        sum_current_item = value[0] * value[1]

        if counter >= 5:
            break

        if sum_current_item > budget:
            continue

        else:
            counter += 1
            budget -= sum_current_item
            result += f"You bought {name} for {sum_current_item:.2f} leva.\n"

    return result










print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))