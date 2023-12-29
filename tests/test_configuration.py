from kafkapy.properties import KafkaProtocolProperties

def test_can_set_item() -> None:
    properties = KafkaProtocolProperties({})
    properties['bootstrap.servers'] = 'localhost:9092'
    assert properties['bootstrap.servers'] == 'localhost:9092'

def test_bootstrapped_properties() -> None:
    properties = KafkaProtocolProperties(properties=dict(a=100, b=200))
    assert properties == {"a": 100, "b": 200}

def test_config_successfully_loaded() -> None:
    ...


def test_bootstrap_servers_overwrites_config() -> None:
    ...


def test_default_config_lookup_is_correct() -> None:
    ...


def test_no_default_lookup_occurs_if_config_provided() -> None:
    ...