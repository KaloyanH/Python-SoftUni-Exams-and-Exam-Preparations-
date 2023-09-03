import re

pattern = r"([@#])([A-Za-z]{3,})\1(\1)([A-Za-z]{3,})\1"

sentence = input()

words = []
counter = 0
matches = re.finditer(pattern, sentence)
valid_words = False
valid_matches = False

for match in matches:
    if match:
        valid_words = True
        counter += 1
        first_word = match.group(2)
        second_word = match.group(4)
        if first_word == second_word[::-1]:
            words.append(f"{first_word} <=> {second_word}")
            valid_matches = True

if valid_words:
    print(f"{counter} word pairs found!")
    if valid_matches:
        print("The mirror words are:")
        print(", ".join(words))
    else:
        print("No mirror words!")
else:
    print("No word pairs found!")
    print("No mirror words!")

