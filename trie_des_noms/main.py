from pathlib import Path

FILE_PATH = Path.cwd() / "trie_des_noms" / "prenom.txt"

with open (FILE_PATH, "r", encoding="utf-8") as f: 
    names = f.read().strip()
    
names = sorted(names.replace("\n", ", ").replace("\t ", ", ").split(", "))

List = []
for i in  names:
    List.append(i.strip())

List = sorted(List) 

SAVE_FILE = FILE_PATH.parent/"prenom_tries.txt"

with open(SAVE_FILE, "w", encoding="utf-8") as save_file:
    for name in List:
        save_file.write(name + "\n")