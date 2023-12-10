import typer


partitions_app = typer.Typer(
    help=":star: [green][bold]Partition Inspection & Management[/green][/bold]", rich_markup_mode="rich"
)


@partitions_app.command()
def list():
    """List"""
