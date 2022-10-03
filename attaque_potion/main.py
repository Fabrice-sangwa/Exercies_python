import random 

your_life_points = enemy_s_life_points = 50
commands =  ["1", "2"]
potion = 3

while True : 
    answer = input("Souhaitez-vous attaquer (1) ou utiliser une potion (2) ?\n>")
    if  not answer.isdigit() or not answer in commands: 
        continue
    elif answer == "1" : 
        your_domage_point = random.randint(5, 10)
        her_domage_point = random.randint(5, 15)
        
        your_life_points -= her_domage_point
        enemy_s_life_points -= your_domage_point
        
        print(f"Vous avez infligé {your_domage_point} points de dégats l'ennemi")
        print(f"L'ennemi vous a infligé {her_domage_point} de dégats")
        
        if your_life_points <= 0 :
            print("Vous avez perdu, Game over")
            break
        elif enemy_s_life_points <= 0 :
            print("Vous avez gagné !")
            break
        else : 
            print(f"Il vous reste {your_life_points} points de vie.")
            print(f"Il reste {enemy_s_life_points} points de vie à l'ennemi.")
            print("-"*37)
                
    elif answer == "2":
        if potion > 0: 
            potion_points = random.randint(15, 50)
            potion -= 1
            your_life_points += potion_points
            
            print(f"Vous avez récupérez {potion_points} points de vie({potion} potions restantes)")
            
            her_domage_point = random.randint(5, 15)
            your_life_points -= her_domage_point
            
            print(f"L'ennemi vous a infligé {her_domage_point} points de dégats")
            
            if enemy_s_life_points <= 0 :
                print("Vous avez gagné !")
                break
            elif your_life_points <= 0 :
                print("Vous avez perdu, Game over")
                break
            else : 
                print(f"Il vous reste {your_life_points} points de vie.")
                print(f"Il reste {enemy_s_life_points} points de vie à l'ennemi.")
                print("-"*37)
                
                print("Vous passez votre tour...")
                
                her_domage_point = random.randint(5, 15)
                your_life_points -= her_domage_point
                
                print(f"L'ennemi vous a infligé {her_domage_point} de dégats")
                
                if your_life_points <= 0 :
                    print("Vous avez perdu, Game over")
                    break
                elif enemy_s_life_points <= 0 :
                    print("Vous avez gagné !")
                    break
                else : 
                    print(f"Il vous reste {your_life_points} points de vie.")
                    print(f"Il reste {enemy_s_life_points} points de vie à l'ennemi.")
                    print("-"*37)
                     
        elif potion <= 0 : 
                print("Vous n'avez plus de potion. ")
                continue
            
    
               
        