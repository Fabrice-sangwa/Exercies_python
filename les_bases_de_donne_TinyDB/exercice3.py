from tinydb import TinyDB, Query, where

db = TinyDB("data_1.json", indent=4)


#créer une table spécifique
users = db.table("Users")
roles = db.table("Roles")

users.insert({"name" : "Skin", "salary" : 23_000})
users.insert({"name" : "Patrick", "salary" : 18_000})
users.insert({"name" : "James", "salary" : 20_000})

roles.insert_multiple([
    {"name" : "CEO"},
    {"name" : "Programmer"},
    {"name" : "Designer"}
])
