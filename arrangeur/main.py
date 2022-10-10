from pathlib import Path

dirs = {".jpg": "Images",
        ".gif": "Images",
        ".mp4": "Videos",
        ".pdf": "Documents",
        ".mp3": "Musiques",
        ".wav": "Musiques"}

tri_dir = Path.home() / "Tri"
files = [f for f in tri_dir.iterdirs() if f.is_file()]
for f in files:
    # Si aucune correspondance n'est trouvé pour l'extension, on place les fichiers dans un dossier Autres
    output_dir = tri_dir / dirs.get(f.suffix, "Autres")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)