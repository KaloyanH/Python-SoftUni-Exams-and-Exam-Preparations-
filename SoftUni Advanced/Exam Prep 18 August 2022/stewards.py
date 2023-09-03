from collections import deque

sequence_of_seats = input().split(", ")
first_seq = deque([int(x) for x in input().split(", ")])
second_seq = [int(x) for x in input().split(", ")]

matched_seats = 0
rotations = 0
taken_seats = []

while True:

    if matched_seats >= 3:
        break

    if rotations >= 10:
        break

    rotations += 1

    sum_seats = chr(first_seq[0] + second_seq[-1])
    seat_one = f"{first_seq[0]}{sum_seats}"
    seat_two = f"{second_seq[-1]}{sum_seats}"

    if seat_one in taken_seats or seat_two in taken_seats:
        first_seq.popleft()
        second_seq.pop()
        continue

    if seat_one in sequence_of_seats and seat_one not in taken_seats:
        taken_seats.append(seat_one)
        matched_seats += 1
        first_seq.popleft()
        second_seq.pop()

    elif seat_two in sequence_of_seats and seat_two not in taken_seats:
        taken_seats.append(seat_two)
        matched_seats += 1
        first_seq.popleft()
        second_seq.pop()

    else:
        value_one = second_seq.pop()
        second_seq.insert(0, value_one)
        first_seq.append(first_seq.popleft())

print(f"Seat matches: {', '.join(str(x) for x in taken_seats)}")
print(f"Rotations count: {rotations}")
