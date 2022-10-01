import os

chemin = r"C:\Users\Fabrice\Desktop\Cours Udemy\Python\Exercices\module_os"
dossier = os.path.join(chemin, "dossier", "Aa")

if not os.path.exists(dossier): 
    os.makedirs(dossier)
else : 
    print("Le dossier existe déjà")
    
    


if os.path.exists(dossier):
    os.removedirs(dossier)
else : 
    print("Le n'existe pas")
