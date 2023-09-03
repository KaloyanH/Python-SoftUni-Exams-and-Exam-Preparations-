list_of_books = input().split("&")

while True:

    command = input().split(" | ")

    if command[0] == "Done":
        break

    if command[0] == "Add Book":
        current_book = command[1]
        if current_book in list_of_books:
            continue
        else:
            list_of_books.insert(0, current_book)

    if command[0] == "Take Book":
        current_book = command[1]
        if current_book not in list_of_books:
            continue
        else:
            list_of_books.remove(current_book)

    if command[0] == "Swap Books":
        first_book = command[1]
        second_book = command[2]
        if first_book not in list_of_books:
            continue
        elif second_book not in list_of_books:
            continue
        else:
            index_first_book = list_of_books.index(first_book)
            index_second_book = list_of_books.index(second_book)
            list_of_books[index_first_book], list_of_books[index_second_book] \
                = list_of_books[index_second_book], list_of_books[index_first_book]

    if command[0] == "Insert Book":
        current_book = command[1]
        if current_book in list_of_books:
            continue
        else:
            list_of_books.append(current_book)

    if command[0] == "Check Book":
        index = int(command[1])
        if 0 < index <= len(list_of_books):
            current_book = list_of_books[index]
            print(current_book)
        else:
            continue

print(", ".join(list_of_books))
