def words_sorting(*args):

    words_dict = {}
    result = ""
    sorted_dict = {}
    for word in args:
        for element in word:
            if word not in words_dict:
                words_dict[word] = 0
            words_dict[word] += ord(element)

    if sum(words_dict.values()) % 2 == 0:
        sorted_dict = dict(sorted(words_dict.items(), key=lambda x: x[0]))

    elif sum(words_dict.values()) % 2 != 0:
        sorted_dict = dict(sorted(words_dict.items(), key=lambda x: -len(x[0])))

    for key, value in sorted_dict.items():
        result += f"{key} - {value}\n"

    return result



print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))