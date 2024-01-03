import typer

from .constants import AppHelp

consumer_groups_application = typer.Typer(
    name="consumer-groups",
    help=AppHelp.CONSUMER_GROUPS_DESCRIPTION,
    rich_markup_mode="rich",
)


@consumer_groups_application.command()
def list():
    """List"""
