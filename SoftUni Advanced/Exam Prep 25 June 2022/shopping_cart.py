def shopping_cart(*args):
    result = ""
    menu = {

        "Soup": [],
        "Pizza": [],
        "Dessert": []

        }

    for argument in args:
        if argument == "Stop":

            break

        meal, product = argument[0], argument[1]

        if meal == "Soup":
            if len(menu["Soup"]) == 3:
                continue
            if product not in menu["Soup"]:
                menu["Soup"].append(product)

        elif meal == "Pizza":
            if len(menu["Pizza"]) == 4:
                continue
            if product not in menu["Pizza"]:
                menu["Pizza"].append(product)

        elif meal == "Dessert":
            if len(menu["Dessert"]) == 2:
                continue
            if product not in menu["Dessert"]:
                menu["Dessert"].append(product)

    if all(len(j) == 0 for j in menu.values()):
        return "No products in the cart!"

    sorted_menu = dict(sorted(menu.items(), key=lambda x: (-len(x[1]), x[0])))

    for key, values in sorted_menu.items():
        result += f"{key}:\n"
        for value in sorted(values):
            result += f" - {value}\n"

    return result


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
