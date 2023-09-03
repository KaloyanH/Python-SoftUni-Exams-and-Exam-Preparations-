def best_list_pureness(*args):

    rotations = args[-1]
    num_list = args[0]

    max_sum = 0
    rotation = 0

    for idx in range(rotations + 1):

        current_sum = 0
        current_rotation = idx
        for index, value in enumerate(num_list):
            current_sum += index * value

        if current_sum > max_sum:
            max_sum = current_sum
            rotation = current_rotation

        last_element = num_list.pop()
        num_list.insert(0, last_element)


    return f"Best pureness {max_sum} after {rotation} rotations"

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)