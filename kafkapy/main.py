import typer
import typing
from topics import topics_app
from partitions import partitions_app
from consumer_groups import consumer_groups_app
from typing_extensions import Annotated
from acls import acls_app
from callbacks import version_callback

app = typer.Typer(help="Python CLI for managing kafka clusters.", rich_markup_mode="rich")
app.add_typer(topics_app, name="topics")
app.add_typer(partitions_app, name="partitions")
app.add_typer(consumer_groups_app, name="consumer-groups")
app.add_typer(acls_app, name="access-controls")


@app.callback(help="Below are the supported top level options and [bold]subcommands[/bold] available.")
def main(
    version: Annotated[bool, typer.Option(help="View the installed kafapy version", callback=version_callback)],
    brokers: Annotated[typing.List[str], typer.Option(help="Bootstrap (broker) host:port")] = ["localhost:9092"],
    client_id: Annotated[str, typer.Option(help="The user agent, recorded in backend kafka logs.")] = "kafkapy",
    verbose: Annotated[bool, typer.Option(help="Enable verbose output.")] = False,
) -> None:
    ...


if __name__ == "__main__":
    app()
