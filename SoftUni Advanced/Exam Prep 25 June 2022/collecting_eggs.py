from  collections import deque

egg = deque([int(x) for x in input().split(", ")])
paper = [int(x) for x in input().split(", ")]

box_size = 50
boxes_filled = 0

while egg and paper:

    if egg[0] <= 0:
        egg.popleft()
        continue

    if egg[0] == 13:
        egg.popleft()
        value = paper.pop()
        paper.insert(0, value)
        continue

    if egg[0] + paper[-1] <= box_size:
        boxes_filled += 1
        egg.popleft()
        paper.pop()

    else:
        egg.popleft()
        paper.pop()


if boxes_filled > 0:
    print(f"Great! You filled {boxes_filled} boxes.")

else:
    print(f"Sorry! You couldn't fill any boxes!")

if egg:
    print(f"Eggs left: {', '.join(str(x) for x in egg)}")

if paper:
    print(f"Pieces of paper left: {', '.join(str(x) for x in paper)}")
