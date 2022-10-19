import json

fichier = "data.json"

with open(fichier, "r") as f:
    data = json.load(f)
    

data["age"] = 50

with open(fichier, "w") as f : 
    json.dump(data, f, indent=4)