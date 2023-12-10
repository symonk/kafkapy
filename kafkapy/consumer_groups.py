import typer


consumer_groups_app = typer.Typer(
    help=":star2: [green][bold]Consumer Groups Inspection & Management[/green][/bold]", rich_markup_mode="rich"
)


@consumer_groups_app.command()
def list():
    """List"""
