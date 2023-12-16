import typer
import typing
from kafkapy.topics import topics
import pathlib
from kafkapy.consumer_groups import consumers
from kafkapy.brokers import brokers
from typing_extensions import Annotated
from kafkapy.parsers import path_to_properties_converter
from kafkapy.acls import acls
from kafkapy.config import KafkaProtocolProperties
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
root_help = ":star2: [green][bold]Kafkapy Loaded.[/][/] [b]Homepage: [green][b][link=https://www.github.com/symonk/kafkapy]https://github.com/symonk/kafkapy[/link][/][/]"

# The handling for the  --version option.
root_version_cmd = typer.Option(
    "--version", help=VERSION_OPTION_HELP, callback=version_callback, is_eager=True
)

# The handling for the --brokers option.
root_brokers_cmd = typer.Option(help="[b][white]The list of available brokers.[/][/]")


# The handling for the --verbose option.
root_verbose_cmd = typer.Option("--verbose", help="Output verbosely.")

root_client_config = typer.Option(
    "--properties",
    help="The .yaml file to use for client instantiation, overrides other flags.",
    parser=path_to_properties_converter,
)


@app.callback(help=root_help)
def main(
    ctx: typer.Context,
    version: Annotated[bool, root_version_cmd] = False,
    brokers: Annotated[typing.List[str], root_brokers_cmd] = ["localhost:9092"],
    properties_file: Annotated[
        KafkaProtocolProperties, root_client_config
    ] = pathlib.Path("~/.kafkapy/properties.yaml"),
    verbose: Annotated[bool, root_verbose_cmd] = False,
) -> None:
    """The main callback is responsible for handling reusable options that
    almost every subcommand requires.  It is also responsible for initializing
    a singleton client."""
    client_from_context(ctx=ctx, properties=properties_file)


if __name__ == "__main__":
    app()
