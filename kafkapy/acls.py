import typer
from kafkapy.constants import AppHelp


acls = typer.Typer(
    help=AppHelp.ACL_DESCRIPTION,
    rich_markup_mode="rich",
)
