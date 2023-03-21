# AppSignal Python

[![PyPI - Version](https://img.shields.io/pypi/v/appsignal-python.svg)](https://pypi.org/project/appsignal-python)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/appsignal-python.svg)](https://pypi.org/project/appsignal-python)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install appsignal
```

## Development

AppSignal for Python uses [Hatch](https://hatch.pypa.io/latest/) to manage dependencies, packaging and development environments.

```sh
pip install hatch
```

### Linting and type checking

```sh
hatch run lint:all

hatch run lint:fmt # auto-formatting only
hatch run lint:style # style checking only
hatch run lint:typing # type checking only
```

### Running tests

```sh
hatch run test:pytest
```

### Running the CLI command

```sh
hatch shell
appsignal
```

### Building wheels

```sh
hatch run build:all # for all platforms
hatch run build:me # for your current platform
hatch run build:for <triple> # for a specific agent triple
```

### Clean up build artifacts
```sh
hatch clean # clean dist folder
rm -r tmp # clean agent build cache
```
