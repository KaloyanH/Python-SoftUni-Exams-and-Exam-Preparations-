def flights(*args):

    flight = {}

    for item in range(0, len(args), 2):
        if args[item] == "Finish":
            break
        else:
            if args[item] not in flight:
                flight[args[item]] = 0
            flight[args[item]] += int(args[item + 1])

    return flight



print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))


# {'Vienna': 282, 'Morocco': 98, 'Paris': 115}
# {'London': 0, 'New York': 309, 'Aberdeen': 215, 'Sydney': 2, 'Nice': 0}
# {}
