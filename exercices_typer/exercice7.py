import typer
import time


def main():
    numbers = range(100)
    
    #pour pouvoir afficher une barre de progression sur l'évolution de notre boucle on va utiliser un con
    #manager qui va encapsuler la boucle 

    with typer.progressbar(numbers) as progress:
        for number in progress:
            time.sleep(0.05)

    typer.secho("Fin du script", fg=typer.colors.BRIGHT_BLUE)


if __name__ == "__main__":
    typer.run(main) 
    