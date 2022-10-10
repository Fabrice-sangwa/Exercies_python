
"""

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

print(entreprise["employees_list"][1]["name"])
print(entreprise.get("employees_list"))    
"""
films = {
    "Le Seigneur des Anneaux" : 12,
    "Harry Potter" : 9,
    "Blade Runner" : 7.5
}

#del films["Blade Runner"]
films["Le Seigneur des Anneaux"] = 80
prix = films["Le Seigneur des Anneaux"] + films["Harry Potter"] + films["Blade Runner"]
print(prix)
print(list(films.keys()))
print(list(films.values))