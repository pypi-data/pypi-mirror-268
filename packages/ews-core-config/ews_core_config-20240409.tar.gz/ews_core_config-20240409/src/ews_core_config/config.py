from __future__ import annotations

import logging
import os
import socket
import subprocess
from copy import deepcopy
from pathlib import Path

import tomlkit

logging.getLogger("simple_toml_configurator").setLevel(logging.ERROR)
logging.getLogger("Configuration").setLevel(logging.ERROR)
from simple_toml_configurator import Configuration  # noqa: E402

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

hostname = socket.gethostname().upper()

name = email = gh_username = ""
try:
    p = subprocess.run(
        "git config --get user.name",  # noqa: S607
        shell=True,  # noqa: S602
        capture_output=True,
        text=True,
        check=False,
    )
    if not p.returncode:
        name = p.stdout.strip()
    p = subprocess.run(
        "git config --get user.email",  # noqa: S607
        shell=True,  # noqa: S602
        capture_output=True,
        text=True,
        check=False,
    )
    if not p.returncode:
        email = p.stdout.strip()
        gh_username = "ews-" + email.split("@")[0].replace(".", "")
except Exception as e:
    raise e
finally:
    pass


DEFAULT_CONFIG = {
    "sharepoint": {
        "server": "ewsconsulting.sharepoint.com",
        "site": "https://ewsconsulting.sharepoint.com/sites/teams_mb/",
        "username": email,
        "password": "",
    },
    "github": {
        "username": gh_username,
        "token": "",
    },
    "ewstools": {
        "url": "https://mb.ews.tools",
        "host": "smufcm.ews.local",
        "port": "52812",
        "username": "mb_upload",
        "password": "",
    },
    "ammonitor": {
        "username": "wm@ews-consulting.com",
        "password": "",
    },
    "windcubeinsights": {
        "username": "wm@ews-consulting.at",
        "password": "",
    },
    "paths": {
        "mount_point": "/mnt",
        "drives": "c;d;f;p;r",
        "mappings": "/ews.local/GLOGBAL/Daten:f;/ews.local/GLOBAL/QM:p;/smuffile001/daten$:f;/smuffile001/qm$:p;/smuffile001/ROHDATEN$:r",  # noqa: E501
    },
    "wheelhouse": {
        "local": {
            "devpi": {
                "hostname": hostname,
                "port": 8051,
                "index": "root/private",
                "index_url": "root/all/+simple",
            },
            "pyserver": {
                "hostname": hostname,
                "port": 8050,
                "index": "",
                "index_url": "simple",
            },
        },
        "global": {
            "pyserver": {
                "hostname": "WMUFS100",
                "port": 3140,
                "index": "",
                "index_url": "simple",
            },
            "devpi": {
                "hostname": "WMUFS100",
                "port": 3141,
                "index": "root/private",
                "index_url": "root/all/+simple",
            },
        },
    },
}


def recursive_pop(val, parent=None, key=None):  # noqa: C901
    has_parent = parent and key
    if isinstance(val, dict):
        if not val and has_parent:
            parent.pop(key)
            return None
        new_vals = deepcopy(val)
        keys = list(new_vals.keys())
        for k in keys:
            recursive_pop(new_vals[k], parent=new_vals, key=k)
        if has_parent:
            if new_vals:
                parent[key] = new_vals
            else:
                parent.pop(key)
                return None
        return new_vals
    elif isinstance(val, list):
        if not val and has_parent:
            parent.pop(key)
            return parent
        new_vals = []
        for _, v in enumerate(val):
            new_v = recursive_pop(v)
            if new_v is not None:
                new_vals.append(new_v)

        if has_parent:
            if new_vals:
                parent[key] = new_vals
            else:
                parent.pop(key)
                return None
        return new_vals
    elif isinstance(val, str):
        v = val.strip()
        if not v and has_parent:
            parent.pop(key)
        return None
    elif val is None:
        if has_parent:
            parent.pop(key)
        return None
    else:
        return val


def clean_dashes(val):
    if isinstance(val, dict):
        keys = list(val.keys())
        for k in keys:
            if "-" in k:
                logger.debug(f"Keys with dashes - are not allowed! (key: {k!r})")
                if k.replace("-", "_") in keys:
                    val.pop(k)
                    continue
            clean_dashes(val[k])
    elif isinstance(val, list):
        for _, v in enumerate(val):
            clean_dashes(v)


def merge(source, destination):
    """
    run me with nosetests --with-doctest file.py

    >>> a = { 'first' : { 'all_rows' : { 'pass' : 'dog', 'number' : '1' } } }
    >>> b = { 'first' : { 'all_rows' : { 'fail' : 'cat', 'number' : '5' } } }
    >>> merge(b, a) == { 'first' : { 'all_rows' : { 'pass' : 'dog', 'fail' : 'cat', 'number' : '5' } } }
    True
    """
    for key, value in source.items():
        if isinstance(value, dict):
            # get node or create one
            node = destination.setdefault(key, {})
            merge(value, node)
        else:
            destination[key] = value

    return destination


class _EWSSettings(Configuration):
    def __init__(self, create_if_inexistent: bool = True, update: bool = True) -> None:
        config_path = os.environ.get("EWS_CONFIG_PATH", Path.home() / ".config" / "ews")
        config_file_name = os.environ.get("EWS_CONFIG_FILENAME", ".ews_config")
        filename = Path(config_path) / f"{config_file_name}.toml"
        existing = {}

        if filename.is_file():
            logger.info("Reading defaults from existing file")
            existing = tomlkit.loads(filename.read_bytes())

        if not existing:
            if create_if_inexistent:
                logger.warn("Creating new file")  # pragma: no cover
                existing = deepcopy(DEFAULT_CONFIG)
        else:
            if update:
                existing = recursive_pop(existing)
            existing = merge(existing, DEFAULT_CONFIG)

        if filename.is_file():
            filename.unlink()

        clean_dashes(existing)

        super().__init__(
            config_path=config_path,
            config_file_name=config_file_name,
            defaults=existing,
            env_prefix="EWS",
        )


def read_settings(create_if_inexistent: bool = True, update: bool = True) -> _EWSSettings:
    return _EWSSettings(create_if_inexistent=create_if_inexistent, update=update)


__all__ = ("_EWSSettings", "read_settings")
