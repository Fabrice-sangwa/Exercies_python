def somme (a , b ):
    return f"La somme de {a} + {b} = {a + b} "  

def division(a, b):
    try :
        return  f"La division de {a}/{b} = { round(a / b, 3)}" 
    except:
        return f"Pas de division possible pour ce cas"

def multiplication(a , b):
    return f"La multiplication de {a} * {b} = {a * b} "  

def soustraction(a, b):
    return f"La soustraction de {a} - {b} = {a - b} "  

def run ():

    options = ["a", "s", "m", "d", "q"]
    
    while True : 
        choise = input("Entrez le choix, m : multiplication, a : addition , s : soustraction , d : division, q : quitter\n>")
        
        if not choise in options:
            continue 
        elif choise == "q":
            break
        else :
            a = int(input("Veuillez saisir le premier nombre : "))
            b = int(input("Veuillez saisir le deuxième nombre : "))
            
            if choise == "a":
                print(somme(a, b))
            elif choise == "s":
                print(soustraction(a,b))
            elif choise == "m":
                print(multiplication(a,b))
            elif choise == "d":
                print(division(a,b))
                
            continue
        
run()
        