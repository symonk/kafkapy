from kafkapy.config import KafkaProtocolProperties
from kafkapy.out import write_err
import pathlib
import yaml


def path_to_properties_converter(path: str) -> KafkaProtocolProperties:
    """Given a path on the command line to a file, build the properties
    class with the file, or assume a sensible default."""
    path = pathlib.Path(path)
    default_props = KafkaProtocolProperties(
        {"bootstrap.servers": "localhost:9092", "client.id": "kafkapy"}
    )
    if path.exists:
        try:
            with path.open(mode="r") as outfile:
                properties = yaml.safe_load(outfile.read())
                return KafkaProtocolProperties(properties)
        except Exception as exc:  # Todo: Dont catch wide exceptions
            write_err("Falling back to using default settings because: ", exc)
            return default_props
    return default_props
