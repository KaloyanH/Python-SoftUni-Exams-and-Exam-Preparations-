import re

text = input()

cool_threshold = 1

for char in text:
    if char.isdigit():
        cool_threshold *= int(char)

pattern = r"(:{2}|\*{2})([A-Z][a-z]{2,})(\1)"

searched_emoji = re.findall(pattern, text)

cool_words = []
all_words = []

if searched_emoji:
    for word in searched_emoji:
        current_word = word[0] + word[1] + word[2]
        all_words.append(current_word)
        word_threshold = 0
        for char in word[1]:
            word_threshold += ord(char)
        if word_threshold >= cool_threshold:
            cool_words.append(current_word)


print(f"Cool threshold: {cool_threshold}")
if all_words:
    print(f"{len(all_words)} emojis found in the text. The cool ones are:")

if cool_words:
    for word in cool_words:
        print(word)

