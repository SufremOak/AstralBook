import typer
from rich import print
from rich.console import Console
from astrlsh import AstralShell
from AstralTui import AstralTui

app = typer.Typer()

@app.command()
def start(tui: bool = typer.Option(False, "--tui", help="Start in TUI mode")):
    if tui:
        tui = AstralTui()
        tui.run()
    else:
        shell = AstralShell()
        shell.run()


if __name__ == "__main__":
    app()
