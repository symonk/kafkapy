import typer
from colors import in_white


topics_app = typer.Typer(help="Manage Topics")


@topics_app.command(rich_help_panel=in_white("Topic Inspection & Management :snake:"))
def list():
    """[blue]List all available topics and exit.[/blue]"""