import typer
import rich

app = typer.Typer(
    help="Python CLI for managing kafka clusters.",
    rich_markup_mode="rich")

@app.command(rich_help_panel="Checks")
def check():
    """Execute various checks."""
    typer.Exit(code=0)

@app.callback()
def main(verbose: bool = False):
    """
    Entrypoint.
    """
    if verbose:
        ...
        
if __name__ == "__main__":
    app()