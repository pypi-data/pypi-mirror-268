# RedXClient

![coverage](https://gitlab.com/codesigntheory/redxclient/badges/main/coverage.svg?job=test)

A [Pydantic](https://docs.pydantic.dev/latest/)-powered client for the [RedX Courier service's API](https://redx.com.bd/).

## Features
    - Support for all public API endpoints
    - Responses are returned as Pydantic models, making it easy to work with the data.
    - Properly type-hinted for optimal IDE support and DX.


## Installation

```bash
pip install redxclient
```

## Usage

```python
from redxclient import RedXClient

client = RedXClient(api_key="your_api_key") # You can pass the base_url as well, by default it uses the sandbox url

parcel = client.get_parcel_details("parcel_id")
print(parcel)
```

You can find all the `schemas` in the schema module of the package.

## Development

To install the development version, clone the repository and install the package in editable mode:

```bash
git clone
cd redxclient
pdm sync -d
```
