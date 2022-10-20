import typer


def main(delete: bool = typer.Option(False, help="Supprime les fichiers trouvés"), extension: str  = typer.Argument(None, help="Exetenstion à chercher")):
    """ 
        Afficher les fichiers trouvés avec leur extension de données 
    """
    #typer.echo(f"Recherche des fichiers avec l'extension {extension}")
    
    #demander une valeur dans la ligne de commande
    #extension = typer.prompt("Quelle exstension souhaitez-vous chercher")
    #print(extension)
    
    #on souhaite faire une demade de confirmation avant la suppression 
    if delete:
        confirm = typer.confirm("Voulez-vous vraiment supprimer le fichier ? ")
        if not confirm:
            typer.echo("opération annulée")
            raise typer.Abort()
    print("Suppression des fichiers")
    
    
if __name__ == "__main__":
    typer.run(main) 