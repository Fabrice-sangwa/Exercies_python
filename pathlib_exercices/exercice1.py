from pathlib import Path

#Dossier utilisateur 
print(Path.home())

#Dossier courant à partir duquel on a lancé l'interpreteur
print(Path.cwd())

#concatener des chemins 
p = Path.cwd()
p = p / "Documents" / "main.py"
print(p.suffix)

#Autres suffix
print("*" * 10)
print(p.name)
print(p.stem)
print(p.suffix)
print(p.parent)
print(p.suffixes)
print(list(p.parts))
print(p.exists())
print(p.is_dir())
print(p.is_file())
