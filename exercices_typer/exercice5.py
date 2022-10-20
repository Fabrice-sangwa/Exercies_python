import typer

app = typer.Typer()

def main(delete: bool = typer.Option(False, help="Supprime les fichiers trouvés"), extension: str  = typer.Argument(None, help="Exetenstion à chercher")):
    """ 
        Afficher les fichiers trouvés avec leur extension de données 
    """
    
    if delete:
            confirm = typer.confirm("Voulez-vous vraiment supprimer le fichier ? ")
            if not confirm:
                typer.echo("opération annulée")
                raise typer.Abort()
            else:
                print(f"Suppression des fichiers avec l'extension {extension}")
    else :
        typer.echo(f"Recherche de fichiers avec l'extension {extension}")
        
@app.command("seach")
def seach_py():
    main(delete=False, extension="py")


@app.command("delete")
def delete_py():
    main(delete=True, extension="py")


    
if __name__ == "__main__":
    #typer.run(main) 
    
    app()