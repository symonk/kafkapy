from rich import print
import typer
import yaml
import pathlib
import io
from kafkapy.config import KafkaProtocolConfiguration
from kafkapy.__version__ import __version__
from kafkapy.constants import LibraryMeta


def version_callback(value: bool) -> str:
    """Prints the version of kafkapy and exits."""
    if value:
        print(
            f"[white][bold]{LibraryMeta.NAME.title()}[/white][/bold] [green][bold]{__version__}[/green][/bold] [yellow][bold]:zap:[/yellow][/bold]"
        )
        raise typer.Exit(code=0)


def load_properties(value: pathlib.Path) -> KafkaProtocolConfiguration:
    """Attempt to (safely) load the resolved .yaml file provided and
    shovel it into the configuration object."""
    if value.exists:
        try:
            with io.open(value, "w", encoding="utf-8") as outfile:
                properties = yaml.safe_dump(outfile)
                return KafkaProtocolConfiguration(properties)
        except Exception:  # Todo: Dont catch wide exceptions
            return KafkaProtocolConfiguration({})
