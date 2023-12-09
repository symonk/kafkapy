import typer


app = typer.Typer(
    help="",
    rich_markup_mode="rich")


@app.command()
def list():
    """List the topics available."""