import json
import logging
from os import makedirs


import constants

Logger = logging.getLogger()


class List(list):
    
    def __init__(self, list_name):
        self.list_name = list_name
    
    
    def ajouter (self, element):
        
        if not isinstance(element, str):
            raise ValueError("Vous ne pouvez ajouter que des chaine de caractère ! ")
        
        if element in self :
            Logger.error(f"{element} est déjà dans la liste de {self.list_name}")
            return False
        
        self.append(element)
        return True
    
    def enlever(self, element):
        if element in self:
            self.remove(element)
            return True
        return False
    
    def afficher(self):
        print(f"Le contenu de ma liste de {self.list_name} :")
        print("-"*34)
        for number, element in enumerate(self):
            print(f"{number + 1}. {element}")
        
    def sauvegarder(self):
        chemin = constants.CUR_DIR / f"{self.list_name}.json"
        if not chemin.exists():
            chemin.touch()
        
        with open (chemin, "w") as f:
            json.dump(self, f, indent=4)
    
        return True
    
if __name__ == "__main__":
    liste = List("Courses")
    result = liste.ajouter("Banane")
    result = liste.ajouter("Sauce")
    result = liste.ajouter("Tomates")
    result = liste.ajouter("Sucre")
    result = liste.ajouter("Sel")
    result = liste.ajouter("Miel")
    result = liste.ajouter("Papaye")

    liste.sauvegarder()

    if result : 
        liste.afficher()
    
        
        
        
        
    