
import typer
 

from pathlib import Path
#ce module permet de rendre un parmaètre optionnel
from typing import Optional


app = typer.Typer()

@app.command("run")
def main(extension: str, 
         directory: Optional[str] = typer.Argument(None, help="Dossier dans lequel chercher"),
         delete: bool = typer.Option(False, help="Supprime les fichiers trouvés")):
    
    """
        Affiche les fichiers trouvés et leurs extension passé en paramètre
    """
    #Vérification si le dossier n'est pas passé en paramètre
    if directory:
        directory = Path(directory)
    else:
        directory = Path.cwd()
    
    if not directory.exists():
        typer.secho(f"Le dossier '{directory}' n'existe pas.", fg=typer.colors.BRIGHT_RED)
        raise typer.Exit()
    
    files = directory.rglob(f"*{extension}")
    
    if delete:
        confirm = typer.confirm("Voulez-vous vraiment supprimer ces fichiers ?")
        if confirm :
            for file in files:
                file.unlink()
                typer.secho(f"Suppression du fichier {file}", fg=typer.colors.BRIGHT_RED)
                
            typer.secho(f"Les fichiers de l'extension {extension} ont été supprimés", fg=typer.colors.BRIGHT_GREEN)
        else:
            typer.secho("opération annulée", fg=typer.colors.GREEN)
            raise typer.Abort()
            
    else:
        typer.secho(f"Fichier trouvé avec l'extension {extension}:", bg=typer.colors.BLUE, fg=typer.colors.BRIGHT_WHITE)
        for file in files:
            typer.secho(file, fg=typer.colors.BRIGHT_GREEN)


@app.command("search")
def search(extension: str):
    """Chercher les fichiers avec l'extension donnée"""
    main(extension=extension, directory=None, delete=False)
    
@app.command("delete")
def delete(extension: str):
    """Supprimer les fichiers avec l'extension donnée"""
    main(extension=extension,directory=None,delete=True)

if __name__ == "__main__":
    app()