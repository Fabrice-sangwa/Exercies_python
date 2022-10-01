liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric", "Maxime"]


position = liste.index("Maxime") 
print(position)

occurence = liste.count("Maxime")
print(occurence)

liste.sort()
print(liste)

liste = ["Maxime", "Martine", " Christopher", "Carlos", "Michael", "Eric", "Maxime", "Til   "]
liste_triee = sorted(liste)
print(liste_triee)


liste.reverse()
print(liste)