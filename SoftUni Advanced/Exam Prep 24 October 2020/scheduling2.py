jobs = [int(x) for x in input().split(", ")]
job_index = int(input())

searched_number = jobs[job_index]
cycles = 0

for index, job in enumerate(jobs):
    if searched_number >= job and job_index != index:
        cycles += job

print(cycles + searched_number)
