import sqlite3


connexion = sqlite3.connect("databas.db")

curseur = connexion.cursor()


d = {"id" : 1, "nom" : "Paul", "prenom" : "Dupond"}
curseur.execute("insert into employees values (:id, :nom, :prenom)", d)

connexion.commit()
connexion.close()