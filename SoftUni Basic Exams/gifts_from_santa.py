second_number = int(input())
fist_number = int(input())
address_number = int(input())

for addresses in range(fist_number, second_number - 1, -1):
    if addresses % 2 == 0 and addresses % 3 == 0:
        if addresses == address_number:
            break
        else:
            print(addresses, end=" ")
