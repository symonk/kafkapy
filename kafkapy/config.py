from dataclasses import dataclass
import typing


@dataclass
class Configuration:
    """The runtime configuration."""

    brokers: typing.List[str]
    client_id: str
    verbose: bool
