from re import L


chemin = input(r"Veuillez Saisir le chemin d'accès du fichier : ")
 
try:
    with open(chemin, "r") as f:
        print(f.read())
except UnicodeDecodeError:
    print("Il est impossible d'ouvrir ce type de fichier.")
except FileNotFoundError:
    print(f"{chemin} est introuvable.")
except:
    print("Une erreur est survenue")