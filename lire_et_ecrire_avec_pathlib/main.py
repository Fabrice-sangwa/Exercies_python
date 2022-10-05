from cgitb import text
from pathlib import Path

p = Path.cwd()/"lire_et_ecrire_avec_pathlib" / "read_dir"

p.mkdir(exist_ok=True)

p /= "Texte.txt"

p.touch(exist_ok=True)

p.write_text("Je veux bien rire !")
texte = p.read_text()
print(texte)
