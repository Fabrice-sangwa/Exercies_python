from random import randint

print("***Le jeu du nombre mystère***")
line = "-" * 40
tests = 5
print(f"Il te reste {tests} essaies")

mystery_number = randint(1, 100)


while True:
    if tests == 0:
        print(f"Tu as atteint la limite !\nLe nombre mystère était {mystery_number}\nGame over")
        break
    else : 
        answer = input("Devine le nombre : ")
        if not answer.isdigit() or len(answer.strip()) == 0 : 
            answer = input("Entrez une réponse correcte")
            continue
        else: 
            if int(answer) > mystery_number :
                print("Un peu plus petit que ça")
                tests -= 1
                if tests != 0:
                    print(f"Il te reste {tests} essaies")
                    print(line) 
                else : 
                    continue  
            elif int(answer) < mystery_number : 
                print("Un peu plus grand que ça")
                tests -= 1
                if tests != 0:
                    print(f"Il te reste {tests} essaies")
                    print(line)
                else : 
                    continue
            elif int(answer) == mystery_number :
                print(f"Bravo ! Tu as trouvé le nombre mystère en {tests} essaies")
                break
