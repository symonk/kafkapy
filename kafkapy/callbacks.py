import typing

import typer

from .__version__ import __version__
from .constants import LibraryMeta
from .out import write_out
from .types import BootstrapServersTypes


def version_callback(ctx: typer.Context, value: bool) -> str:
    """Prints the version of kafkapy and exits."""
    if ctx.resilient_parsing:
        return
    if value:
        write_out(
            f"[white][bold]{LibraryMeta.NAME.title()}[/white][/bold] [green][bold]{__version__}[/green][/bold] [yellow][bold]:zap:[/yellow][/bold]"
        )
        raise typer.Exit(0)


def bootstrap_servers_callback(
    servers: BootstrapServersTypes,
) -> typing.Optional[str]:
    """Validate the bootstrap servers (if provided) by the users.

    :param servers: (Optional) list of colon delimited broker servers and their port."""
    if not servers:
        return None

    for broker in servers:
        if broker.count(":") > 1:
            raise typer.BadParameter("cannot contain more than 1 ':'")
    return ",".join(servers)
