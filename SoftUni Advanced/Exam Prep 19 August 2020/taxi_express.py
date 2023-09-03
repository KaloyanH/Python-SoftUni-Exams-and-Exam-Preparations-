from collections import deque

customers = deque([int(x) for x in input().split(", ")])
taxis = [int(x) for x in input().split(", ")]

total_time = 0


while customers:

    customer_time = customers.popleft()
    if taxis:
        taxi_time = taxis.pop()
    else:
        customers.appendleft(customer_time)
        break

    if taxi_time >= customer_time:
        total_time += customer_time

    else:
        customers.appendleft(customer_time)

if customers:
    print(f"Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")

else:
    print(f"All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")
