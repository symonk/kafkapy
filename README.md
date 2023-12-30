<img src="https://github.com/symonk/kafkapy/blob/main/.github/images/logo.png" border="1" width="275" height="275">

![version](https://img.shields.io/pypi/v/kafkapy?color=%2342f54b&label=&style=flat-square)
[![codecov](https://codecov.io/gh/symonk/kafkapy/branch/main/graph/badge.svg)](https://codecov.io/gh/symonk/kafkapy)
[![docs](https://img.shields.io/badge/documentation-online-brightgreen.svg)](https://symonk.github.io/kafkapy/)

###  Kafkapy

A python command line interface for inspection and management of a kafka cluster.  `kafkapy` is a single utility
for all management and inspection actions.  I wrote this tool when working with `AWS MSK` as dealing with many
different utility scripts from confluence was combersome and often required additional pre/post processing of the
data which is not in a suitable format for piping etc, thus `kafkapy` was born.

`kafkapy` aims to implement all the actions supported by the confluence utility scripts, but also plans to build in
testability for common tasks, such as calculating the sum of all offset lag across all partitions for a topic etc.

All output from `kafkapy` to `stdout` is fully compliant `json` and suitable for piping to tools etc.


> [!CAUTION]
> `Kafkapy` requires broker versions 0.11.0.0 or greater. 


-----

## Quick Start

`kafkapy` is very simple to use, you need two simple things to get started.

```console
# install the python package:
pip install kafkapy

# to get started:
kafkapy --help
```

> [!TIP]
> Ensure your kafka cluster is up and running.

In order to interact with kafka, you should create a `properties.yaml` file on disk and provide it's path to
any commands, the `properties.yaml` file will honour any `librdkafka` properties.  By default `kafkapy` will
look inside `~/.kafkapy/properties.yaml` as a fallback should you not provide the option explicitly via
`--properties`.   

Additionally all commands take an (Optional) `--bootstrap-servers` (List) option which you can specify the
broker addresses manually, these are also available via `librdkafka` config via the `bootstrap.servers` property
so can reside in your `properties.yaml` file if you so choose. 

> [!TIP]
> Ensure your `~/.kafkapy/properties.yaml` contains appropriate properties for auth etc.

View `librdkafka` properties [Here](https://github.com/confluentinc/librdkafka/blob/master/CONFIGURATION.md)

> [!TIP]
> `kafkapy` looks great, but when piping to other tooling colour is automatically excluded for unix compatibility 

-----

## User Guide

> [!TIP]
> For full examples, visit the user guide at: https://symonk.github.io/kafkapy/

-----

## Contributing

If you want to contribute with Kafkapy check out the Contributing Guide to learn how to start.