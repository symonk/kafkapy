from rich import print
import typer
import yaml
import pathlib
import rich
from kafkapy.config import KafkaProtocolProperties
from kafkapy.__version__ import __version__
from kafkapy.constants import LibraryMeta


def version_callback(value: bool) -> str:
    """Prints the version of kafkapy and exits."""
    if value:
        print(
            f"[white][bold]{LibraryMeta.NAME.title()}[/white][/bold] [green][bold]{__version__}[/green][/bold] [yellow][bold]:zap:[/yellow][/bold]"
        )
        raise typer.Exit(code=0)


def load_properties(path: pathlib.Path) -> KafkaProtocolProperties:
    """Attempt to (safely) load the resolved .yaml file provided and
    shovel it into the configuration object."""
    default_props = KafkaProtocolProperties(
        {"bootstrap_servers": "localhost:9092", "client_id": "kafkapy"}
    )
    if path.exists:
        try:
            with path.open(mode="r") as outfile:
                properties = yaml.safe_load(outfile.read())
                return KafkaProtocolProperties(properties)
        except Exception as exc:  # Todo: Dont catch wide exceptions
            rich.print(
                "kafkapy had trouble parsing the properties file, using defaults because: ",
                exc,
            )
            return default_props
    return default_props
