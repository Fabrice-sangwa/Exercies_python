import typer


def main(delete: bool = typer.Option(False, help="Supprime les fichiers trouvés"), extension: str  = typer.Argument(None, help="Exetenstion à chercher")):
    """ 
        Afficher les fichiers trouvés avec leur extension de données 
    """
    typer.echo(f"Recherche des fichiers avec l'extension {extension}")
    
    
if __name__ == "__main__":
    typer.run(main) 