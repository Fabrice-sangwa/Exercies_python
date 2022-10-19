import sqlite3

connexion = sqlite3.connect("database.db")

curseur = connexion.cursor()

"""

curseur.execute("""      
"""create table if not exists enseignants
(
    nom text, 
    prenom text, 
    age int,
    salaire int, 
    matricule text
                      
)
"""
""")

d = {"nom" : "Danult", "prenom" : "Patick", "age" : 28,  "salaire" :3200,  "matricule": "PDA345"}
curseur.execute("insert into enseignants values (:nom, :prenom, :age, :salaire, :matricule)", d)

"""

d = {"nom" : "Danult", "prenom" : "Patick", "age" : 28,  "salaire" :4000,  "matricule": "PDA345"}
curseur.execute("UPDATE enseignants  SET salaire=:salaire WHERE prenom=:prenom AND nom=:nom AND matricule=:matricule", d)

connexion.commit()
connexion.close()
