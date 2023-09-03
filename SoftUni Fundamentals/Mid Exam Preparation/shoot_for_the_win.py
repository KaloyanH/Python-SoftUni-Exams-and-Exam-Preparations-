targets = list(map(int, input().split()))
count_targets = 0

while True:

    command = input()

    if command == 'End':
        break

    index = int(command)

    if index < 0 or index >= len(targets):
        continue
    else:
        count_targets += 1
        number_to_remove = targets[index]
        targets = [x + number_to_remove if x <= number_to_remove and x != -1 else x - number_to_remove\
            if x > number_to_remove and x != 1 else x for x in targets]
        targets[index] = -1

print(f"Shot targets: {count_targets} ->", *targets, sep=' ')
