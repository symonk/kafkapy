import typer

TOPIC_NAME_ARGUMENT = typer.Argument(
    "--topic",
    help="The particular topic to lookup information of, all topics if not provided.",
)

TOPIC_CONFIG_ARGUMENT = typer.Option(
    "--topic-config",
    help="The per-topic configuration, if omitted the topic server defaults will be applied.",
)
