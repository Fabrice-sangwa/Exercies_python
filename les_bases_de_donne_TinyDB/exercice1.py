from tinydb import TinyDB, Query, where

db = TinyDB("data.json", indent=4)

#objet requete de la classe querry
requete = Query()

#recupérer toutes les données qui concerne james
james_data = db.search(requete.name=='James') 
print(james_data)      

#récuperer des données unique sous forme de dictionnaire
venar_data = db.get(requete.name=='Venar') 
print(venar_data)      
                                       

#connaître le nombre d'éléments dans la base de données
print(len(db))

#on peut aussi rechercher des données de cette manière 
skin_data = db.search(where("name") == "Skin")
print(skin_data[0]["score"])

#verifier si un élément est dans la bse de données
print(db.contains(requete.name == "Skin"))

#afficher un certain nombre d'éléments qui rencontrent une condition
print(db.count(requete.score >= 200))
 