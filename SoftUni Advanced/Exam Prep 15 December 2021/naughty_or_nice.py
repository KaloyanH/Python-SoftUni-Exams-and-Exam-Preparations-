def return_funct(list1, list2, list3):
    result = ""

    if list1:
        result += f"Nice: {', '.join(list1)}\n"
    if list2:
        result += f"Naughty: {', '.join(list2)}\n"
    if list3:
        result += f"Not found: {', '.join(list3)}"

    return result


def naughty_or_nice_list(*args, **kwargs):

    kids_list = args[0]

    nice_list = []
    naughty_list = []
    not_found_list = []

    for argument in args[1:]:
        number, mood = argument.split("-")
        counter = 0
        current_name = ""
        element_to_remove = ""
        for element in kids_list:
            if element[0] == int(number):
                counter += 1
                current_name = element[1]
                element_to_remove = element
        if counter == 1:
            if mood == "Nice":
                nice_list.append(current_name)

            elif mood == "Naughty":
                naughty_list.append(current_name)
            kids_list.remove(element_to_remove)

    for name, mood in kwargs.items():
        counter = 0
        current_name = ""
        element_to_remove = ""

        for element in kids_list:

            if element[1] == name:
                counter += 1
                current_name = element[1]
                element_to_remove = element
        if counter == 1:
            if mood == "Nice":
                nice_list.append(current_name)

            elif mood == "Naughty":
                naughty_list.append(current_name)
            kids_list.remove(element_to_remove)

    if kids_list:
        for kid in kids_list:
            not_found_list.append(kid[1])

    return return_funct(nice_list, naughty_list, not_found_list)

#
# print(naughty_or_nice_list(
#     [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy")], "3-Nice", "1-Naughty", Amy="Nice", Katy="Naughty",
# ))
# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
#     ))

# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))