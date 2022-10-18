import sqlite3


connexion = sqlite3.connect("databas.db")

curseur = connexion.cursor()


d = {"prenom" : "Dupond"}
curseur.execute("select * from employees where prenom=:prenom", d)
data = curseur.fetchall()
print(data)

connexion.commit()
connexion.close()