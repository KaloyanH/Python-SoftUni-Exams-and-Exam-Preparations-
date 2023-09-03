from collections import deque

eggs = deque([int(x) for x in input().split(", ")])
paper = [int(x) for x in input().split(", ")]

boxes = 0

while eggs and paper:

    if eggs[0] <= 0:
        eggs.popleft()
        continue

    if eggs[0] == 13:
        eggs.popleft()
        paper[0], paper[-1] = paper[-1], paper[0]
        continue

    if (eggs[0] + paper[-1]) <= 50:
        boxes += 1
        eggs.popleft()
        paper.pop()

    else:
        eggs.popleft()
        paper.pop()

if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")
if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
if paper:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper)}")