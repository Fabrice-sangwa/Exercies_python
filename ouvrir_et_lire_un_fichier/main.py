
import json


chemin = "text.txt"
"""
with open(chemin, "r", encoding="UTF-8") as f : 
    text = f.read().splitlines()
print(text)


chemin = "text_write.txt"

with open (chemin, "a") as f:
    f.write("Salut !")
""" 
chemin = r"ouvrir_et_lire_un_fichier\text.json"
with open(chemin, "r")  as f:
    #json.dump(list(range(1,11)), f, indent=4)
    liste  = json.load(f)
    print(liste)
    
