###  Kafkapy

Kafkapy is a python kafka administrative tool for managing brokers and other resources brokers manage such as
`topics` and `partitions`.  

-----

## Quick Start

Create a `kafkapy.yaml` file, by default `kafkapy` will look in `~/.kafkapy/properties.yaml` if one is not
provided via `--properties`.  This file should set any of the properties you wish to pass on to the underlying
`librdkafka` library options.

For a full properties reference, see the following:

[https://github.com/confluentinc/librdkafka/blob/master/CONFIGURATION.md]


-----

## Contributing