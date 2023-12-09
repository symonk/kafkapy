import typer


consumer_groups_app = typer.Typer(help="Manage Consumer Groups")


@consumer_groups_app.command()
def list():
    """List"""
