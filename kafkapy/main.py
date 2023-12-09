import typer
import time
from rich.progress import track


app = typer.Typer(
    help="Python CLI for managing kafka clusters.",
    rich_markup_mode="rich")

@app.command()
def check(boostrap_server: str, group: str):
    """Execute various checks."""
    typer.Exit(code=0)

@app.command()
def other():
    """Placeholder."""

@app.callback()
def main(verbose: bool = False):
    """
    A Suite of utilities for managing a [bold][red]kafka[/bold][/red] cluster.
    """


if __name__ == "__main__":
    app()