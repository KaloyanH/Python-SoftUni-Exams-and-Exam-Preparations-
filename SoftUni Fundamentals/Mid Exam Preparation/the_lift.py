people_waiting = int(input())
state_of_the_lift = input().split()
lift_capacity = 4
the_lift = []

for i, e in enumerate(state_of_the_lift):
    people_in_wagon = int(e)

    while True:
        if people_in_wagon >= lift_capacity:
            the_lift.append(people_in_wagon)
            break
        if people_waiting < 1:
            the_lift.append(people_in_wagon)
            break
        people_in_wagon += 1
        people_waiting -= 1

full_lift = set(the_lift)

if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(*the_lift, sep=" ")

elif people_waiting == 0 and full_lift == {4}:
    print(*the_lift, sep=" ")

else:
    print("The lift has empty spots!")
    print(*the_lift, sep=" ")
