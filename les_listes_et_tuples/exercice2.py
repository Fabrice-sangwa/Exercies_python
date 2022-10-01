
liste = ["Fabrice", "SANGWA", 1_000_000_000]
print(liste)

liste.append("il")
print(liste)

liste.extend(["Un", "deux", 3, 4, 5])
print(liste)

liste.remove("deux")
print(liste)

premier_element = liste[0]
deuxime_element = liste[1]
print(premier_element)
print(deuxime_element)