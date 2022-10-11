
films = {
    "Le Seigneur des Anneaux" : 12,
    "Harry Potter" : 9,
    "Blade Runner" : 7.5
}

#del films["Blade Runner"]
films["Le Seigneur des Anneaux"] = 80
prix = films["Le Seigneur des Anneaux"] + films["Harry Potter"] + films["Blade Runner"]
print(prix)
print(list(films.keys()))
print(list(films.values))