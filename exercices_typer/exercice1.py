import typer


def main():
    """ 
        Afficher les fichiers trouvés avec leur extension de données 
    """
    
    #Afficher un message dans le terminal lors du lancement
    typer.echo(f"Recherche des fichiers avec l'extension")
    
#indiquer ce que l'on souhaite exécuter

if __name__ == "__main__":
    typer.run(main) 
    