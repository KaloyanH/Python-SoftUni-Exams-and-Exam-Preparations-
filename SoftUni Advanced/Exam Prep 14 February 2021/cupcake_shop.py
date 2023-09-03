def stock_availability(*args):
    cookies = args[0]
    command = args[1]

    if command == "delivery":
        for item in args[2:]:
            cookies.append(item)

    elif command == "sell":
        for item in args[2:]:
            if isinstance(item, int):
                cookies = cookies[item:]


            else:
                for item in args[2:]:
                    while item in cookies:
                        cookies.remove(item)

        if len(args) == 2:
            cookies.remove(cookies[0])


    return cookies




print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

# ['choco', 'vanilla', 'banana', 'caramel', 'berry']
# ['chocolate', 'vanilla', 'banana', 'cookie', 'banana']
# ['vanilla', 'banana']
# []
# ['banana']
# ['cookie', 'banana']
# ['chocolate', 'vanilla', 'banana']