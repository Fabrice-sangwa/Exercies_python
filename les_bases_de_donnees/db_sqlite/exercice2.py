import sqlite3


connexion = sqlite3.connect("database.db")

curseur = connexion.cursor()


d = {"id" : 3, "nom" : "ML", "prenom" : "Jean"}
curseur.execute("insert into employees values (:id, :nom, :prenom)", d)

connexion.commit()
connexion.close()