total_price = 0
amount_of_taxes = 0
price_without_taxes = 0

while True:
    current_command = input()
    amount_of_taxes = total_price - price_without_taxes
    if current_command == "special":
        total_price -= total_price * 0.1
        break
    if current_command == "regular":
        break

    if float(current_command) <= 0:
        print("Invalid price!")
        continue

    price_without_taxes += float(current_command)
    total_price += float(current_command) + float(current_command) * 0.2


if total_price <= 0:
    print("Invalid order!")

else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_taxes:.2f}$")
    print(f"Taxes: {amount_of_taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price:.2f}$")
