def numbers_searching(*args):
    new_list = []
    numbers = sorted(int(x) for x in args)
    missing_element = [item for item in range(numbers[0], numbers[-1]+1) if item not in numbers]
    dupes = [x for x in numbers if numbers.count(x) > 1]
    for i in dupes:
        if i not in new_list:
            new_list.append(i)

    missing_element.extend([new_list])

    return missing_element

print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
