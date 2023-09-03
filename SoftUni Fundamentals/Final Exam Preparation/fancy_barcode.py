import re

lines = int(input())

pattern = r"^(@{1}#+)([A-Z]{1}[A-Za-z0-9]{4,}[A-Z]{1})@{1}#+"

for _ in range(lines):

    barcodes = input()

    searched_barcode = re.search(pattern, barcodes)
    if searched_barcode:
        barcode = searched_barcode.group(2)
        if any(ch.isdigit() for ch in barcode):
            digits = ""
            for digit in barcode:
                if digit.isdigit():
                    digits += digit
            print(f"Product group: {digits}")
        else:
            print("Product group: 00")

    else:
        print("Invalid barcode")
