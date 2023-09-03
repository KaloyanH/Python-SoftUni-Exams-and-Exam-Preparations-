from collections import deque

pizza_orders = deque([int(x) for x in input().split(", ")])
employees = [int(x) for x in input().split(", ")]

total_pizzas = 0

while employees and pizza_orders:

    if pizza_orders[0] > 10:
        pizza_orders.popleft()
        continue

    if pizza_orders[0] <= 0:
        pizza_orders.popleft()
        continue

    if pizza_orders[0] <= employees[-1]:
        total_pizzas += pizza_orders[0]
        pizza_orders.popleft()
        employees.pop()

    elif pizza_orders[0] > employees[-1]:
        total_pizzas += employees[-1]
        pizza_orders[0] -= employees[-1]
        employees.pop()

if not pizza_orders:
    print(f"All orders are successfully completed!""\n"f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")
else:
    print(f"Not all orders are completed.""\n"f"Orders left: {', '.join(str(x) for x in pizza_orders)}")
