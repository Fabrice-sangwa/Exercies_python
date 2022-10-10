films = {
    "La casa de papel " : 18.4,
    "Les 6 voyous" : 50,
    "Les 4 fantastiques " : 38,
    "Avengers " : 19,
    "Black Panther " : 80,
    "Soldat de l'hyver" : 70
}

print("Les prix des films ce soir")
print("-"*25)
for key, value in films.items():
    print(key, str(value)+ "$")