import typer
from rich import print
from rich import print_json
import sys
import typing
from .client import Serializable


def write_out(data: typing.Union[str, Serializable], *args, **kwargs):
    """Use rich to nicely print to stdout.

    :param data: The data to write out."""
    print_json(check_is_serializable(data), *args, **kwargs)


def write_err(data: typing.Union[str, Serializable], *args, **kwargs):
    """Use rich to nicely print to stderr.

    :param data: The data to write out."""
    print(check_is_serializable(data), *args, **kwargs, file=sys.stderr)


def die(code: int, message: str) -> None:
    """Write an error to stderr and exit.

    :param code: The exit code.
    :param message: The error message."""
    write_err(message)
    raise typer.Exit(code)


def check_is_serializable(obj: typing.Union[str, Serializable]) -> str:
    """Check if the object is implements serializable and get its str representation.

    :param object: An object to attempt to serialize."""
    if isinstance(obj, Serializable):
        return obj.as_json()
    return obj
