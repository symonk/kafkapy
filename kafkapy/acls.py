import typer

from .constants import AppHelp

acls_application = typer.Typer(
    name="access controls",
    help=AppHelp.ACL_DESCRIPTION,
    rich_markup_mode="rich",
)
