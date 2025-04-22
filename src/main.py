import typer
from rich import print
from rich.console import Console
from astrlsh import AstralShell

app = typer.Typer()

@app.command()
def start():
    shell = AstralShell()
    shell.run()


if __name__ == "__main__":
    app()
