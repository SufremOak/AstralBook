from rich.console import Console
from rich.markdown import Markdown
import numpy as np
from math.algebra import AlgebraInterpreter
from math.algebra import BasicOperations

class AstralShell:
    def __init__(self):
        self.console = Console()
        self.running = True

    def start(self):
        self.console.print("[bold cyan]Welcome to the Astral Shell![/]", style="bold")
        self.console.print("[dim]Type 'help' for commands. Type 'exit' to quit.[/]")

    def handle_command(self, command):
        command = command.strip().lower()
        if command == 'exit':
            self.console.print("[yellow]Goodbye![/]")
            self.running = False
        elif command == 'help':
            self.console.print("[bold green]Available commands:[/]")
            self.console.print("  [cyan]help[/] - Show this help message")
            self.console.print("  [cyan]exit[/] - Exit the shell")
        elif command == '':
            pass
        else:
            self.console.print(f"[red]Unknown command:[/] {command}")

    def run(self):
        self.start()
        while self.running:
            try:
                command = input("AstralShell> ")
                self.handle_command(command)
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Use 'exit' to quit[/]")
            except EOFError:
                break
