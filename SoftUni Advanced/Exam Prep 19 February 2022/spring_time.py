def start_spring(**kwargs):
    my_dict = {}
    result = ""
    for key, value in kwargs.items():
        if value not in my_dict:
            my_dict[value] = []
        my_dict[value].append(key)

    sorted_dict = dict(sorted(my_dict.items(), key=lambda x:  ((-len(x[1])), -len(x[0]), x[0])))

    for key, values in sorted_dict.items():
        result += f"{key}:\n"
        for value in sorted(values):
            result += f"-{value}\n"

    return result
