liste = ["Utilisateur_01",
         "Utilisateur_02",
         "Utilisateur_03",
         "Utilisateur_04",
         "Utilisateur_05",
         "Utilisateur_06",
         "Utilisateur_07"
         ]
print(liste[:])
print(liste[::-1])
print(liste[:3:3])
print(liste[3::2])
print(liste[1:-1])
print(liste)

liste = ["Maxime", "Martine", "Christopher", "Carlos", "Michael", "Eric"]
trois_premiers = liste[:3]
trois_derniers = liste[3:]
milieu = liste[1:-1]
premier_dernier = liste[::5]

print(trois_premiers)
print(trois_derniers)
print(milieu)
print(premier_dernier)
