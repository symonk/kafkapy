import pathlib

from kafkapy.parsers import path_to_properties_converter


def test_loading_yaml_file() -> None:
    properties = path_to_properties_converter(
        pathlib.Path(__file__).parent.joinpath("assets").joinpath("properties.yaml")
    )
    assert properties.get("bootstrap.servers") == "test:9092"
    assert properties.get("client.id") == "testkafkapy"


def test_defaults_without_gets() -> None:
    properties = path_to_properties_converter(
        pathlib.Path().joinpath("doesnotexist"), use_default=False
    )
    assert properties.get("bootstrap.servers") == "localhost:9092"
    assert properties.get("client.id") == "kafkapy"
