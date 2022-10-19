import sqlite3


connexion = sqlite3.connect("database.db")

curseur = connexion.cursor()


#d = {"prenom" : "Dupond"}where prenom=:prenom, d
curseur.execute("select * from employees")
data = curseur.fetchall()
print(data)

connexion.commit()
connexion.close()