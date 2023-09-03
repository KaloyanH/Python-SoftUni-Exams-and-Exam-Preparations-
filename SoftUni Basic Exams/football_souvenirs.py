country_name = input()
type_souvenirs = input()
number_souvenirs = int(input())

souvenir_price = 0

if country_name == "Argentina":
    if type_souvenirs == "flags":
        souvenir_price = 3.25
    elif type_souvenirs == "caps":
        souvenir_price = 7.20
    elif type_souvenirs == "posters":
        souvenir_price = 5.10
    elif type_souvenirs == "stickers":
        souvenir_price = 1.25
elif country_name == "Brazil":
    if type_souvenirs == "flags":
        souvenir_price = 4.20
    elif type_souvenirs == "caps":
        souvenir_price = 8.50
    elif type_souvenirs == "posters":
        souvenir_price = 5.35
    elif type_souvenirs == "stickers":
        souvenir_price = 1.2
elif country_name == "Croatia":
    if type_souvenirs == "flags":
        souvenir_price = 2.75
    elif type_souvenirs == "caps":
        souvenir_price = 6.9
    elif type_souvenirs == "posters":
        souvenir_price = 4.95
    elif type_souvenirs == "stickers":
        souvenir_price = 1.1
elif country_name == "Denmark":
    if type_souvenirs == "flags":
        souvenir_price = 3.1
    elif type_souvenirs == "caps":
        souvenir_price = 6.5
    elif type_souvenirs == "posters":
        souvenir_price = 4.80
    elif type_souvenirs == "stickers":
        souvenir_price = 0.9

total_cost = number_souvenirs * souvenir_price

if country_name != "Argentina" and country_name != "Brazil" and country_name != "Croatia" and country_name != "Denmark":
    print("Invalid country!")
elif type_souvenirs != "flags" and type_souvenirs != "caps" and type_souvenirs != "posters" and type_souvenirs != "stickers":
    print("Invalid stock!")
else:
    print(f'Pepi bought {number_souvenirs} {type_souvenirs} of {country_name} for {total_cost:.2f} lv.')
