import sys
import typing

import typer
from pydantic import BaseModel
from rich import print
from rich import print_json

from .client import Serializable
from .types import SerializableInstanceType


def write_out(data: typing.Union[str, Serializable], *args, **kwargs) -> None:
    """use rich to print to stdout.

    :param data: The data to serialize and print
    """
    print(check_is_serializable(data), *args, **kwargs, file=sys.stdout)


def write_json_out(data: SerializableInstanceType, *args, **kwargs) -> None:
    """Use rich to nicely print json to stdout.

    :param data: The data to serialize and print
    """
    print_json(check_is_serializable(data), *args, **kwargs)


def write_err(data: typing.Union[str, Serializable], *args, **kwargs) -> None:
    """Use rich to nicely print to stderr.

    :param data: The data to serialize and print
    """
    print(check_is_serializable(data), *args, **kwargs, file=sys.stderr)


def die(code: int, message: typing.Optional[str] = None) -> None:
    """Write an error to stderr and exit.

    :param code: The exit code.
    :param message: The error message."""
    if message:
        write_err(message)
    raise typer.Exit(code)


def check_is_serializable(obj: SerializableInstanceType, *args, **kwargs) -> str:
    """Check if the object is implements serializable and get its str representation.

    :param object: An object to attempt to serialize."""
    if isinstance(obj, BaseModel):
        return obj.model_dump_json(*args, **kwargs)
    return obj
