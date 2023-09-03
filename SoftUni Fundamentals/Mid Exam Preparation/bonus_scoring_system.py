import math

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

all_students_bonuses = []
all_attendance = []

if number_of_lectures == 0:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')

else:
    for _ in range(number_of_students):
        attendance = int(input())
        all_attendance.append(attendance)
        student_bonus = attendance / number_of_lectures * (5 + additional_bonus)
        all_students_bonuses.append(student_bonus)

    best_attendance = max(all_attendance)
    best_bonus = max(all_students_bonuses)

    print(f"Max Bonus: {math.ceil(best_bonus)}.")
    print(f"The student has attended {best_attendance} lectures.")
