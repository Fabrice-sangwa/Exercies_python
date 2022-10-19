from textwrap import indent
from tinydb import TinyDB
from tinydb.storages import MemoryStorage

#creation sur le disque dur
db_1 = TinyDB("data.json",indent=4)

#pour créer une base de données en mémoire
db_2 = TinyDB(storage=MemoryStorage)


#inserer une donnée
#db_1.insert({"name" : "Skin","score" : 200})


#inérer plusieurs données 
db_1.insert_multiple([
        
        {"name" : "marck","score" : 190},
        {"name" : "peter","score" : 329},
        {"name" : "Cyle","score" : 198},
        {"name" : "Malisse","score" : 50},
        {"name" : "Venar","score" : 100},
        {"name" : "James","score" : 200}
        
])