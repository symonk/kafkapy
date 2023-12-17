![Kafkapy](.github/images/logo.png)

![version](https://img.shields.io/pypi/v/kafkapy?color=%2342f54b&label=&style=flat-square)
[![codecov](https://codecov.io/gh/symonk/kafkapy/branch/main/graph/badge.svg)](https://codecov.io/gh/symonk/kafkapy)
[![docs](https://img.shields.io/badge/documentation-online-brightgreen.svg)](https://symonk.github.io/kafkapy/)

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