
jobs = [int(x) for x in input().split(", ")]
searched_idx = int(input())

cycles = 0


for number in sorted(jobs):
    current_index = jobs.index(number)
    if current_index == searched_idx:
        cycles += number
        break

    else:
        cycles += number
        jobs[current_index] = "x"

print(cycles)

