"""Reusable command line options and arguments.  Rule of thumb
is that options are typically optional and arguments are required.
However, providing no default value for an option will also force
it to the required.  Options denoted with an ellipsis default are
also required."""
import typer

from .callbacks import version_callback
from .parsers import path_to_properties_converter

BOOTSTRAP_SERVERS_OPTION = typer.Option(
    "--bootstrap-servers",
    help="Kafka bootstrap servers, overrides properties if specified.",
    # callback=bootstrap_servers_callback,
)

PROPERTIES_FILE_OPTION = typer.Option(
    "--properties",
    help="Path to the librdkafka properties file (yaml).",
    parser=path_to_properties_converter,
)

VERSION_OPTION = typer.Option(
    "--version",
    help="Print the installed version and exit.",
    callback=version_callback,
    is_eager=True,
)

VERBOSE_OPTION = typer.Option(
    "--verbose",
    help="Output verbosely.",
)

TIMEOUT_IN_SECONDS_OPTION = typer.Option(
    "--timeout-seconds",
    help="The timeout, in seconds.",
)

TOPIC_NAME_OPTION = typer.Option(
    "--topic",
    help="The name of the topic.",
)

OPERATION_TIMEOUT = typer.Option(
    "--operation-timeout",
    help="""The operation timeout in seconds.  This controls how long the request will block on the broker
    waiting for the deletion to propagate in the cluster. Defaults to 0.""",
)

REQUEST_TIMEOUT = typer.Option(
    "--request-timeout",
    help="""The overall request timeout in seconds, including broker lookup, request transmission, operation time and response.
    Defaults to the socket.timeout.ms * 1000""",
)

TOPIC_PARTITION_OPTION = typer.Option(
    "--partitions",
    help="The total number of partitions to create, or -1 if --replica-assignment is not provided.",
)

TOPIC_REPLICATION_FACTOR_OPTION = typer.Option(
    "--replication-factor",
    help="The Replication factor of partitions, or -1 if --replica-assignment is not provided. ",
)

TOPIC_REPLICA_ASSIGNMENT_OPTION = typer.Option(
    "--replication-assignment",
    help="A 2D array with the replication assignment for each partition.",
)

TOPIC_AUTHORIZED_OPERATIONS_OPTION = typer.Option(
    "--include-authorized-operations",
    help="If true, fetches topic ACL Operations.  Off by default.",
)

TIMEOUT_INDEF_SECONDS_OPTION = typer.Option(
    "--timeout",
    help="The maximum response time before timing out, forever by default",
)

TOPICS_NAME_OPTION = typer.Option(
    "--topics",
    help="A list of topics to create.",
)

TOPIC_NAME_OPTION = typer.Option(
    "--topic",
    help="The particular topic to lookup information of, all topics if not provided.",
)

TOPIC_CONFIG_OPTION = typer.Option(
    "--topic-config",
    help="The per-topic configuration, if omitted the topic server defaults will be applied.",
)
