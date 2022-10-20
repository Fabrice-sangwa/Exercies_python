import typer


def main():
    
    prenom = typer.style("Fabrice", fg=typer.colors.BRIGHT_CYAN)
    typer.echo(f"Bonjour {prenom}")



if __name__ == "__main__":
    typer.run(main) 
    