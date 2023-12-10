import typer


consumers = typer.Typer(
    help=":star2: [green][bold]Consumer Groups Inspection & Management[/green][/bold]", rich_markup_mode="rich"
)


@consumers.command()
def list():
    """List"""
