from kafkapy.config import KafkaProtocolProperties
import pathlib
import yaml
import rich


def path_to_properties_converter(path: str) -> KafkaProtocolProperties:
    """Given a path on the command line to a file, build the properties
    class with the file, or assume a sensible default."""
    path = pathlib.Path(path)
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
