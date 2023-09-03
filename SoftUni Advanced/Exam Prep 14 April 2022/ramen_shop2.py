from collections import deque

ramen = [int(x) for x in input().split(", ")]
customers = deque([int(x) for x in input().split(", ")])


while ramen and customers:

    if ramen[-1] == customers[0]:
        ramen.pop()
        customers.popleft()

    elif ramen[-1] > customers[0]:
        ramen[-1] -= customers[0]
        customers.popleft()

    elif ramen[-1] < customers[0]:
        customers[0] -= ramen[-1]
        ramen.pop()

if len(customers) == 0:
    print(f"Great job! You served all the customers.")
    if ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in ramen)}")
else:
    print(f"Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")
