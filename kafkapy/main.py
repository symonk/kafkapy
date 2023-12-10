import typer
import typing
from kafkapy.topics import topics
import pathlib
from kafkapy.consumer_groups import consumers
from kafkapy.brokers import brokers
from typing_extensions import Annotated
from kafkapy.acls import acls
from kafkapy.config import Configuration
from kafkapy.callbacks import version_callback
from kafkapy.utils import client_from_context

app = typer.Typer(
    help="Python CLI for managing kafka clusters.",
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["--help"]},
)
app.add_typer(topics, name="topics")
app.add_typer(consumers, name="consumer-groups")
app.add_typer(acls, name="access-controls")
app.add_typer(brokers, name="brokers")


VERSION_OPTION_HELP: typing.Final[
    str
] = "[white][b]Print the installed version and exit.[/][/]"
CLIENT_ID_OPTION_HELP: typing.Final[str] = ""
root_help = ":star2: [green][bold]Kafkapy Loaded.[/][/] [b]Homepage: [green][b][link=https://www.github.com/symonk/kafkapy]https://github.com/symonk/kafkapy[/link][/][/]"

# The handling for the  --version option.
root_version_cmd = typer.Option(
    "--version", help=VERSION_OPTION_HELP, callback=version_callback, is_eager=True
)

# The handling for the --brokers option.
root_brokers_cmd = typer.Option(help="[b][white]The list of available brokers.[/][/]")

# The handling for the --client-id option.
root_client_id_cmd = typer.Option(
    "--client-id", help="The user agents for backend log referencing."
)

# The handling for the --verbose option.
root_verbose_cmd = typer.Option("--verbose", help="Output verbosely.")

root_client_config = typer.Option(
    "--client-config-file",
    help="The .yaml file to use for client instantiation, overrides other flags.",
)


@app.callback(help=root_help)
def main(
    ctx: typer.Context,
    version: Annotated[bool, root_version_cmd] = False,
    brokers: Annotated[typing.List[str], root_brokers_cmd] = ["localhost:9092"],
    client_config_file: Annotated[pathlib.Path, root_client_config] = "",
    client_id: Annotated[str, root_client_id_cmd] = "kafkapy",
    verbose: Annotated[bool, root_verbose_cmd] = False,
) -> None:
    """The main callback is responsible for handling reusable options that
    almost every subcommand requires.  It is also responsible for initializing
    a singleton client."""
    cfg = Configuration(brokers=brokers, client_id=client_id, verbose=verbose)
    client_from_context(ctx=ctx, config=cfg)


if __name__ == "__main__":
    app()
