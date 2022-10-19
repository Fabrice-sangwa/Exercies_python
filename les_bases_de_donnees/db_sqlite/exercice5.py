import sqlite3

connexion = sqlite3.connect("database.db")

curseur = connexion.cursor()



curseur.execute("DELETE from enseignants where prenom='Marc'")
#curseur.execute("DELETE from enseignants")
connexion.commit()
connexion.close()




