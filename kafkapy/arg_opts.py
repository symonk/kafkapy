"""Reusable command line options and arguments.  Rule of thumb
is that options are typically optional and arguments are required.
However, providing no default value for an option will also force
it to the required.  Options denoted with an ellipsis default are
also required."""
from .callbacks import version_callback
from .parsers import path_to_properties_converter
import typer


BOOTSTRAP_SERVERS_OPTION = typer.Option(
    "--bootstrap-servers",
    help="Kafka bootstrap servers, overrides properties if specified.",
)

PROPERTIES_FILE_OPTION = typer.Option(
    "--properties",
    help="Path to the librdkafka properties file (yaml).",
    parser=path_to_properties_converter,
)

VERSION_OPTION = typer.Option(
    "--version",
    help="Print the installed version and exit.",
    callback=version_callback,
    is_eager=True,
)

VERBOSE_OPTION = typer.Option("--verbose", help="Output verbosely.")

TIMEOUT_IN_SECONDS_OPTION = typer.Option(
    "--timeout-seconds",
    help="The timeout, in seconds.",
)

TOPIC_NAME_OPTION = typer.Option(
    "--topic",
    help="The name of the topic.",
)
