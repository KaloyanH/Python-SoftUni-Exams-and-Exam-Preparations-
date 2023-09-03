def stock_availability(*args):

    cupcakes = args[0]

    if args[1] == "delivery":
        new_boxes = [item for item in args[2:]]
        cupcakes.extend(new_boxes)

    elif args[1] == "sell":
        if len(args) == 2:
            cupcakes = cupcakes[1:]

        elif len(args) > 2:
            if isinstance(args[2], int):
                cupcakes = cupcakes[args[2]:]

            else:
                boxes_to_sell = [item for item in args[2:]]
                for cupcake in boxes_to_sell:
                    while cupcake in cupcakes:
                        cupcakes.remove(cupcake)

    return cupcakes







print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie", "banana"))
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
