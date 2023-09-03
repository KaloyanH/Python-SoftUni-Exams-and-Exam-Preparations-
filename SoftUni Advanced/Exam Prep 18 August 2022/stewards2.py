from collections import deque

sequence = input().split(", ")
first_line = deque([int(x) for x in input().split(", ")])
second_line = [int(x) for x in input().split(", ")]

taken_seats = []
rotations = 0

while rotations < 10 and len(taken_seats) < 3:

        letter = chr(first_line[0] + second_line[-1])

        rotations += 1

        if f"{first_line[0]}{letter}" in sequence:
            if f"{first_line[0]}{letter}" not in taken_seats:
                taken_seats.append(f"{first_line[0]}{letter}")
            first_line.popleft()
            second_line.pop()
        elif f"{second_line[-1]}{letter}" in sequence:
            if f"{second_line[-1]}{letter}" not in taken_seats:
                taken_seats.append(f"{second_line[-1]}{letter}")
            first_line.popleft()
            second_line.pop()

        else:
            first_line.append(first_line.popleft())
            second_line.insert(0, second_line.pop())

print(f"Seat matches: {', '.join(str(x) for x in taken_seats)}")
print(f"Rotations count: {rotations}")