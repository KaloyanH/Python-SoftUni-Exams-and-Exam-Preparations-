from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = [int(x) for x in input().split(", ")]

total_time = 0

while customers and taxis:

    if taxis[-1] >= customers[0]:
        total_time += customers[0]
        customers.popleft()
        taxis.pop()

    else:
        taxis.pop()

if len(customers) == 0:
    print(f"All customers were driven to their destinations""\n"f"Total time: {total_time} minutes")

else:
    print(f"Not all customers were driven to their destinations""\n"f"Customers left: {', '.join(str(x) for x in customers) }")
