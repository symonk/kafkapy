from dataclasses import dataclass
from client import BootstrapServer
import typing


@dataclass
class Configuration:
    """The runtime configuration."""

    brokers: typing.List[BootstrapServer]
    client_id: str
    verbose: bool
