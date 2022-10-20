import typer


def main(extension: str = typer.Argument(..., help="Extension à chercher")):
    """
        Affiche les fichiers selon leurs extensions
    """
    if not extension:
        typer.echo("Pas d'extension passé en paramètre")
    else :
        typer.echo(f"Recherche des fichiers avec l'extension {extension}.")
    
if __name__ == "__main__":
    typer.run(main) 