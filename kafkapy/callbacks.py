import typer

from .__version__ import __version__
from .constants import LibraryMeta
from .out import write_out
from .types import BootstrapServersSplitTypes
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
) -> BootstrapServersSplitTypes:
    """Split the user provided bootstrap servers into appropriate host
    and port for kafka broker connectivity.

    :param servers: (Optional) list of colon delimited broker servers and their port."""
    result = []
    if not servers:
        return result
    for server in servers:
        if server.count(":") > 1:
            raise typer.BadParameter(
                f"{server} can only contain at most a single colon ':'."
            )
        host, _, port = server.partition(":")
        result.append((host, int(port)))
    return result
