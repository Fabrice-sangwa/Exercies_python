films = {
    "La casa de papel " : 18.4,
    "Les 6 voyous" : 50,
    "Les 4 fantastiques " : 38,
    "Avengers " : 19,
    "Black Panther " : 80,
    "Soldat de l'hyver" : 70
}

print("Les prix des films ce soir")
print("-"*25)
for key, value in films.items():
    print(key,":", value, "$")
    
print("-"*25)
entreprise = {
    "employees_list" :{
        1 : {
            "name"  : "Fabrice",
            "last_name" : "SANGWA" 
        }, 
        2 : {
            "name" : "John",
            "last_name" : "Smith"
        },
        3 : {
            "name" : "Patricia",
            "last_name" : "Larson"
        }
        
    }
}

print("Le premier employé :", entreprise["employees_list"][1]["name"])  
print("Le nombre d'employés :",len(entreprise.get("employees_list", "")))