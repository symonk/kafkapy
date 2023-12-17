"""Reusable command line options and arguments.  Rule of thumb
is that options are typically optional and arguments are required.
However, providing no default value for an option will also force
it to the required.  Options denoted with an ellipsis default are
also required."""

import typer


TIMEOUT_IN_SECONDS_OPTION = typer.Option(
    "--timeout-seconds",
    help="The timeout, in seconds",
    default=30,
)

TOPIC_NAME_OPTION = typer.Option(
    "--topic",
    help="The name of the topic",
    default=...,
)
