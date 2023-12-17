import typer
from rich import print
import sys


def write_out(data: str, *args, **kwargs):
    """Use rich to nicely print to stdout.

    :param data: The data to write out."""
    print(data, *args, **kwargs, file=sys.stdout)


def write_err(data: str, *args, **kwargs):
    """Use rich to nicely print to stderr.

    :param data: The data to write out."""
    print(data, *args, **kwargs, file=sys.stderr)


def die(code: int, message: str) -> None:
    """Write an error to stderr and exit.

    :param code: The exit code.
    :param message: The error message."""
    write_err(message)
    raise typer.Exit(code)
