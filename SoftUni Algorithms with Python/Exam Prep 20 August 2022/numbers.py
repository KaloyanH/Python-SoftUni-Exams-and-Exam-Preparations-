def find_ways(target, current_sum, current_list):
    if current_sum == target:
        if current_list[-1] != target:
            print(" + ".join(map(str, current_list)))
        return
    if current_sum > target:
        return

    for num in range(target, 0, -1):
        if not current_list or num <= current_list[-1]:
            find_ways(target, current_sum + num, current_list + [num])


def print_sum_ways(target):
    find_ways(target, 0, [])


# Example usage
input_number = int(input())
print(input_number)
print_sum_ways(input_number)
