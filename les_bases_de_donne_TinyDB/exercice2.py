from tinydb import TinyDB, Query, where

db = TinyDB("data.json", indent=4)

#mettre à jour une information 
#db.update({"score": 40}, where('name') == 'Skin')

#insérer un champ dans la base de donées
#db.update({"role":"Junior"})

#mettre à jour les données d'un champ spécifique
db.update({"role":"Pythonista"}, where('name') == 'Skin')

#mettre à jour ou insérer des données
db.upsert({"name" : "Betsa","score" : 300, "role" : "Pianist"}, where('name') == 'Betsa')

#supprimer unze donnée
db.remove(where('score')<= 100)

#supprimer toutes les données
db.truncate()