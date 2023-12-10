import typer
import typing
from kafkapy.topics import topics_app
from kafkapy.partitions import partitions_app
from kafkapy.consumer_groups import consumer_groups_app
from kafkapy.brokers import brokers_app
from typing_extensions import Annotated
from kafkapy.acls import acls_app
from kafkapy.config import Configuration
from kafkapy.callbacks import version_callback
from kafkapy.client import KafkaClient
from kafka.errors import KafkaError
import rich

app = typer.Typer(help="Python CLI for managing kafka clusters.", rich_markup_mode="rich")
app.add_typer(topics_app, name="topics")
app.add_typer(partitions_app, name="partitions")
app.add_typer(consumer_groups_app, name="consumer-groups")
app.add_typer(acls_app, name="access-controls")
app.add_typer(brokers_app, name="brokers")


@app.callback(help="Below are the supported top level options and [bold]subcommands[/bold] available.")
def main(
    ctx: typer.Context,
    version: Annotated[
        bool,
        typer.Option(
            "--version", help="Prints the installed version and exits.", callback=version_callback, is_eager=True
        ),
    ] = False,
    brokers: Annotated[typing.List[str], typer.Option(help="Bootstrap (broker) host:port")] = ["localhost:9092"],
    client_id: Annotated[str, typer.Option(help="The user agent, recorded in backend kafka logs.")] = "kafkapy",
    verbose: Annotated[bool, typer.Option(help="Enable verbose output.")] = False,
) -> None:
    cfg = Configuration(brokers=brokers, client_id=client_id, verbose=verbose)
    try:
        client = KafkaClient(brokers=cfg.brokers, client_id=cfg.client_id)
    except KafkaError as err:
        rich.print(f"[red][bold]{err.__class__.__name__}[/red][/bold](0 brokers reachable for: {cfg.brokers}).")
        raise typer.Exit(code=1)

    ctx.obj = client


if __name__ == "__main__":
    app()
