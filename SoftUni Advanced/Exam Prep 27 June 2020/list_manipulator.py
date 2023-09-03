def list_manipulator(*args):
    result = []

    if args[1] == "remove":
        if args[2] == "end":
            if len(args) > 3:
                result = args[0][:-args[3]]
                return result
            else:
                args[0].pop()
                result = args[0]
                return result

        elif args[2] == "beginning":
            if len(args) > 3:
                result = args[0][args[3]:]
                return result

            else:
                result = args[0][1:]
                return result

    if args[1] == "add":
        if args[2] == "end":
            my_list = args[0]
            numbers = [int(x) for x in args[3:]]
            if len(args[3:]) > 1:

                my_list.extend(numbers)
            else:
                my_list.append(args[3])
            return my_list

        elif args[2] == "beginning":
            my_list = args[0]
            numbers = [int(x) for x in args[3:]]
            if len(args[3:]) > 1:

                numbers.extend(my_list)
            else:
                my_list.insert(0, args[3])
            return numbers



print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
