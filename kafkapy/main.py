import typer
import typing
from kafkapy.topics import topics
from kafkapy.consumer_groups import consumers
from kafkapy.brokers import brokers
from kafkapy.parsers import path_to_properties_converter
from kafkapy.acls import acls
from kafkapy.arg_opts import VERSION_OPTION

app = typer.Typer(
    help="Python CLI for managing kafka clusters.",
    rich_markup_mode="rich",
    context_settings={"help_option_names": ["--help", "-h"]},
)
app.add_typer(topics)
app.add_typer(consumers)
app.add_typer(acls)
app.add_typer(brokers)


root_help = ":star2: [green][bold]Kafkapy Loaded.[/][/] [b]Homepage: [green][b][link=https://www.github.com/symonk/kafkapy]https://github.com/symonk/kafkapy[/link][/][/]"

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
def root(
    version: typing.Annotated[bool, VERSION_OPTION] = False,
):
    """The core entrypoint point.  Responsible for basic app initialization
    and handling of commands that typically report and exit.  Right now this is
    only responsible for handling the version and exiting."""


if __name__ == "__main__":
    app()
