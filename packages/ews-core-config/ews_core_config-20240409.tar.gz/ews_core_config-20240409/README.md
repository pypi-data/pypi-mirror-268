# ews-core-config

[![PyPI version](https://img.shields.io/pypi/v/ews-core-config.svg)](https://pypi.python.org/pypi/ews-core-config)
[![PyPI - License](https://img.shields.io/pypi/l/ews-core-config.svg)](https://pypi.python.org/pypi/ews-core-config)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ews-core-config.svg)](https://pypi.python.org/pypi/ews-core-config)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/ews-core-config)

<!-- ![Build](https://github.com/EWS-Consulting-Public/ews-core-config/actions/workflows/python-publish.yml/badge.svg?event=push) -->
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Precommit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://pre-commit.com)

## Installation

Install with

```sh
pipx install ews-core-config[cli]
```

## What does it do

It looks for a `.ews_config.toml` file in your home directory.

See an example configuration [in this discussion](https://github.com/EWS-Consulting-Public/ews-core-config/discussions/3).

The default config is found in the file [config.py](https://github.com/EWS-Consulting-Public/ews-core-config/blob/main/src/ews_core_config/config.py#L10).

## Usage

Libraries developed by EWS Consulting can require this package as an optional
dependency under the extra `ews`.

This can be done in the `pyproject.toml` file.

```toml

[project.optional-dependencies]
ews = ["ews-core-config"]
```

This installation will be like:

> pip install ews-my-awesome-library[ews]

Then, in the code:

```python
import contextlib
with contextlib.suppress(ImportError):
    from ews_core_config.config import read_settings
    read_settings()
my_password = os.getenv("EWS_SHAREPOINT_USERNAME", "")
```

This will read your config file and set all the environment variables.

For instance, other libraries (like the one used to retrieve files on our SharePoint) will have access to the env. variable `EWS_SHAREPOINT_USERNAME` and `EWS_SHAREPOINT_PASSWORD`.

Alternatively, you can directly retrieve the `settings` from the module.

```python
from ews_core_config.config import read_settings
EWSSettings = read_settings()
username = EWSSettings.sharepoint_username
assert username != "", "Please set your SharePoint user name!"
```

**This is not the preferred way**. Indeed, it might be easier to refractor
libraries to make them independent of our library if they just use environment variables.

## Installation with pipx

```bash
pipx install .[cli] --editable --force
```
