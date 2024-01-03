import pathlib

import typer
import yaml

from .out import write_err
from .properties import KafkaProtocolProperties


def path_to_properties_converter(
    path: str,
    use_default: bool = True,
) -> KafkaProtocolProperties:
    """Given a path on the command line to a file, build the properties
    class with the file, or assume a sensible default."""
    safe_path = pathlib.Path(path)
    if not safe_path.exists() and use_default:
        # The user provided path does not exist on disk.
        # default to our own ~/.kafkapy/properties.yaml file
        safe_path = pathlib.Path().home() / ".kafkapy" / "properties.yaml"
        if not safe_path.exists():
            # No user provided path could be resolved, the default path does
            # not exist either, for now exit but in future we will allow an
            # environment based directory to be looked up as another fallback.
            write_err(
                "No --properties provided and default ~/.kafkapy/properties.yaml does not exist."
            )
            raise typer.BadParameter("No config file exists.")
    default_props = KafkaProtocolProperties(
        {"bootstrap.servers": "localhost:9092", "client.id": "kafkapy"}
    )
    try:
        with safe_path.open(mode="r") as outfile:
            properties = yaml.safe_load(outfile.read())
            return KafkaProtocolProperties(properties)
    except Exception as exc:  # Todo: Dont catch wide exceptions
        write_err("Falling back to using default settings because: ", exc)
        return default_props
