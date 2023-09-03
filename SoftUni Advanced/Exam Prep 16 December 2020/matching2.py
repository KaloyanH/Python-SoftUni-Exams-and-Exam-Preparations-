from collections import deque



males = [int(x) for x in input().split(" ")]
females = deque([int(x) for x in input().split(" ")])

matches = 0

while males and females:

    below_zero = False
    remove_two = False

    if males[-1] <= 0:
        males.pop()
        below_zero = True

    if females[0] <= 0:
        females.popleft()
        below_zero = True

    if below_zero:
        continue

    if males[-1] % 25 == 0:
        males.pop()
        males.pop()
        remove_two = True

    if females[0] % 25 == 0:
        females.popleft()
        females.popleft()
        remove_two = True

    if remove_two:
        continue

    if males[-1] == females[0]:
        males.pop()
        females.popleft()
        matches += 1
        continue
    else:
        females.popleft()
        males[-1] -= 2


print(f"Matches: {matches}")

if males:
    print(f"Males left: {', '.join(str(x) for x in reversed(males))}")
else:
    print(f"Males left: none")
if females:
    print(f"Females left: {', '.join(str(x) for x in females)}")
else:
    print(f"Females left: none")