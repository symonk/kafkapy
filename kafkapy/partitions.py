import typer


partitions_app = typer.Typer(help="Manage Partitions")


@partitions_app.command()
def list():
    """List"""