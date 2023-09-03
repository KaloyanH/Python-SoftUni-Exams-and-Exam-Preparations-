def forecast(*args):

    result = ""

    weather = {
        "Sunny": [],
        "Cloudy": [],
        "Rainy": []
    }

    for element in args:
        if element[1] in weather:
            weather[element[1]].append(element[0])

    for key, values in weather.items():
        for value in sorted(values):
            result += f"{value} - {key}\n"
    return result



print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))