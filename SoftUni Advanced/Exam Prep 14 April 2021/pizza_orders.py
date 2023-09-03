from collections import deque


pizza_orders = deque([int(x) for x in input().split(", ")])
employees = [int(x) for x in input().split(", ")]

total_pizzas = 0

while employees and pizza_orders:

    invalid_order = False

    if pizza_orders[0] <= 0 and pizza_orders:
        pizza_orders.popleft()
        invalid_order = True

    if pizza_orders:
        if pizza_orders[0] > 10:
            pizza_orders.popleft()
            invalid_order = True

    if invalid_order:
        continue

    if pizza_orders[0] <= employees[-1]:
        total_pizzas += pizza_orders[0]
        pizza_orders.popleft()
        employees.pop()

    else:
        total_pizzas += employees[-1]
        pizza_orders[0] = pizza_orders[0] - employees[-1]
        employees.pop()

if not pizza_orders:
    print(f"All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join(str(x) for x in employees)}")

else:
    print(f"Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")

