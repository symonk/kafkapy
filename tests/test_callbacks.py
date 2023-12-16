import typing
from kafkapy.callbacks import load_properties
from kafkapy.config import KafkaProtocolProperties
import pathlib


def test_loading_yaml_file() -> None:
    properties = load_properties(pathlib.Path(__file__).parent.joinpath("assets").joinpath("properties.yaml"))
    assert properties.bootstrap_servers == "test:9092"
    assert properties.client_id == "testkafkapy"


def test_defaults_without_lookups() -> None:
    properties = load_properties(pathlib.Path().joinpath("doesnotexist"))
    assert properties.bootstrap_servers == "localhost:9092"
    assert properties.client_id == "kafkapy"
    