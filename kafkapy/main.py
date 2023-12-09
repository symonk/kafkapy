import typer
import time
from rich.progress import track


app = typer.Typer(
    help="Python CLI for managing kafka clusters.",
    rich_markup_mode="rich")

@app.command()
def check():
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
    total = 0
    for _ in track(range(10_000), description="[green][bold]initializing[green][bold]"):
        time.sleep(0.01)
        total += 1


if __name__ == "__main__":
    app()