from multiprocessing.forkserver import connect_to_new_process
import sqlite3




connexion = sqlite3.connect("databas.db")

curseur = connexion.cursor()

curseur.execute("""
        CREATE TABLE if not exists employees (
            id int , 
            nom text, 
            prenom text
        )       
                
""")

connexion.commit()
connexion.close()