import typer
from kafkapy.constants import AppHelp


consumers = typer.Typer(
    name="consumer-groups",
    help=AppHelp.CONSUMER_GROUPS_DESCRIPTION,
    rich_markup_mode="rich",
)


@consumers.command()
def list():
    """List"""
