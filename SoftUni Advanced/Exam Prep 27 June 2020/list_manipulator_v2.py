def list_manipulator(*args):
    result = ""

    if args[1] == "remove" and args[2] == "end":
        if len(args[2:]) > 1:
            result = args[0][:-args[3]]
        else:
            result = args[0][:-1]

    elif args[1] == "remove" and args[2] == "beginning":
        if len(args[2:]) > 1:
            result = args[0][args[3]:]
        else:
            result = args[0][1:]

    elif args[1] == "add" and args[2] == "end":
        if len(args[2:]) > 1:
            args_list = args[0]
            new_list = [int(x) for x in args[3:]]
            args_list.extend(new_list)
            result = args_list
        else:
            args_list = args[0]
            result = args_list.append(args[3])

    elif args[1] == "add" and args[2] == "beginning":
        if len(args[2:]) > 1:
            args_list = args[0]
            new_list = [int(x) for x in args[3:]]
            new_list.extend(args_list)
            result = new_list
        else:
            args_list = args[0]
            args[0].insert(0, args[3])
            result = args_list

    return result













print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 3))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 23 , 24, ))
