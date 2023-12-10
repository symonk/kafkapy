import typer
import typing
from kafkapy.topics import topics_app
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
app.add_typer(consumer_groups_app, name="consumer-groups")
app.add_typer(acls_app, name="access-controls")
app.add_typer(brokers_app, name="brokers")


version_help = "test"
root_help = ":star: [green][bold]Kafkapy loaded.[/green]  See available arguments and subcommands below.[/bold]"

# The handling for the  --version option.
root_version_cmd = (
    typer.Option(
        "--version",
        help=version_help,
        callback=version_callback,
        is_eager=True,
    ),
)

# The handling for the --brokers option.
root_brokers_cmd = typer.Option(
    help="Bootstrap (broker) host:port",
)

# The handling for the --client-id option.
root_client_id_cmd = (
    typer.Option(
        help="The user agent, recorded in backend kafka logs.",
    ),
)

# The handling for the --verbose option.
root_verbose_cmd = typer.Option("--verbose", help="Output verbosely.")


@app.callback(help=root_help)
def main(
    ctx: typer.Context,
    version: Annotated[bool, root_version_cmd] = False,
    brokers: Annotated[typing.List[str], root_brokers_cmd] = ["localhost:9092"],
    client_id: Annotated[str, root_client_id_cmd] = "kafkapy",
    verbose: Annotated[bool, root_verbose_cmd] = False,
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
