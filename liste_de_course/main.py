from os import sys


liste = []
options = ["1", "2", "3", "4", "5"]
fonctions = "1: Ajouter un élément à la liste de courses\n2: Retirer un élément de la liste de courses\n3: Afficher les éléments de la liste de courses\n4: Vider la liste de courses\n5: Quitter le programme"
line = "-" * 40
indicator = "\U0001F449"
while True : 
    print(fonctions)
    choise = input(f"Choisissez parmi les 5 options suivantes\n{indicator} ")
    if not choise.isdigit() or not choise in options:
        continue
    else :
        if choise == "1":
            element = input(f"Entrez le nom d'un élément à ajouter à la liste de courses\n{indicator}")
            if element.isdigit() or len(element.strip()) == 0:
                print("Veuillez saisir une valeur correcte")
                print(line)
            else :
                if element in liste:
                    print("Cet élément existe déjà dans la liste")
                    print(line)
                else :
                    liste.append(element)
                    print(f"L'élément {element} a bien été ajouté à la liste.")
                    print(line)
                    
        elif choise == "2":
            element = input(f"Veuillez entrer le nom de l'élément à rétirer de la liste de course\n{indicator} ")
            if  len(element.strip()) == 0:
                print("Veuillez entrer une valeur correcte")
                print(line)
            else : 
                if not element in liste: 
                    print("Cet élément n'est pas dans la liste.")
                    print(line)
                else : 
                    liste.remove(element)
                    print(f"L'élément {element} a bien été rétiré de la liste.")
                    print(line)
            
        elif choise == "3":
            if len(liste) == 0:
                print("La liste est vide.")
                print(line)
            else :
                print("Votre liste contient:")
                for i, element in enumerate(liste):
                    print(f"{i + 1}.{element}")
                print(line)
            
        elif choise == "4":
            answer = input(f"Etes-vous sûr ? y ou n\n{indicator} ")
            while answer !="y" and answer != "n":
                answer = input(f"Erreur choisissez soit y, soit n\n{indicator} ")
            if answer.lower == "y":
                liste.clear()
                print("La liste a été vidée de son contenu.")
                print(line)
            else : 
                print(line)
                          
        elif choise == "5":
            answer = input(f"Voulez-vous quitter ? y ou n\n{indicator} ")
            while answer !="y" and answer != "n":
                answer = input(f"Erreur choisissez soit y, soit n\n{indicator} ")
            if answer== "y":
                print("A bientot")
                sys.exit()   
            else : 
                print(line)
                
            
        
            
            