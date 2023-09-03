def best_list_pureness(*args):
    list = args[0]
    rotations = args[1]
    times = 0
    best_score = 0

    for rotation in range(rotations + 1):
        current_score = 0
        for index, value in enumerate(list):
            current_score += index * value
            if current_score > best_score:
                best_score = current_score
                times = rotation

        list.insert(0, list.pop())

    return f"Best pureness {best_score} after {times} rotations"




# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)

# test = ([7, 9, 2, 5, 3, 4], 3)
# result = best_list_pureness(*test)
# print(result)

# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
# print(result)