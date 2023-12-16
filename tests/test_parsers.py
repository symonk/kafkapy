from kafkapy.parsers import path_to_properties_converter
import pathlib


def test_loading_yaml_file() -> None:
    properties = path_to_properties_converter(pathlib.Path(__file__).parent.joinpath("assets").joinpath("properties.yaml"))
    assert properties.lookup("bootstrap.servers") == "test:9092"
    assert properties.lookup("client.id") == "testkafkapy"


def test_defaults_without_lookups() -> None:
    properties = path_to_properties_converter(pathlib.Path().joinpath("doesnotexist"))
    assert properties.lookup("bootstrap.servers") == "localhost:9092"
    assert properties.lookup("client.id") == "kafkapy"
    