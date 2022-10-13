from os import mkdir
from pathlib import Path


CUR_DIR = Path.cwd() / "createur_des_dossiers"
 
data = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

for PARENT_DIR, elements in data.items():
    for  element in elements:
        DIR = PARENT_DIR + "/" + element
        FINAL_DIR = CUR_DIR / DIR
        FINAL_DIR.mkdir(parents=True, exist_ok=True)
        
