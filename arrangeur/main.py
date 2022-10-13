
from pathlib import Path

#You can add and specify another file extension that you have or want to sort

extensions = {".jpg": "Images",
        ".gif": "Images",
        ".mp4": "Videos",
        ".pdf": "Documents",
        ".mp3": "Musiques",
        ".wav": "Musiques", 
        ".avi": "Videos",
        ".bmp": "Images",
        ".png": "Images",
        ".jpg": "Images",
        ".txt": "Documents",
        ".pptx": "Documents",
        ".csv": "Documents",
        ".xls": "Documents",
        ".odp": "Documents",
        ".pages": "Documents", 
        ".py" : "Python"}    

#you can indicate here the path of the folder to which you want to add storage
DIR_PATH = Path.cwd() / "arrangeur" / "data"


files = [f for f in DIR_PATH.iterdir() if f.is_file]

for file in files : 
        FINAL_DIR = DIR_PATH /extensions.get(file.suffix, "Autres")
        FINAL_DIR.mkdir(exist_ok=True)
        file.rename(FINAL_DIR/file.name)
        
     