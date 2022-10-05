
from pathlib import Path
import shutil


p = Path.cwd()

#créer un repertoire avec des sous dossiers
p =  p / "Dossier_test" / "1" / "2" / "3" / "test.txt"

#concaténation
p =  p / "Dossier_test"

#créeer un repertoire
p.mkdir(exist_ok=True)

p = p / "test.txt"
#créer un fichier
p.touch()

#supprimer un fichier
p.unlink()

p = Path.cwd()

p = p /"A_supprimer"

p.mkdir(exist_ok=True)

p /= "Texte.txt"

p.touch(exist_ok=True)


#Si le repertoire ne contient rien
p.rmdir()

#Pour supprimer le dossier si il contient quelque chose

shutil.rmtree(p.parent)


