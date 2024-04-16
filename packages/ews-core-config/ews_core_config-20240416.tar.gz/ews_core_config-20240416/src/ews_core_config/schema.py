""" """

from __future__ import annotations

import socket
import subprocess
import textwrap

from pydantic import BaseModel, ConfigDict, Field

default_mappings = "".join(
    map(
        textwrap.dedent,
        r"""
    /ews.local/GLOGBAL/Daten:f;
    /ews.local/GLOBAL/QM:p;
    /SRFILEWS001.ews.local/daten$:f;
    /SRFILEWS001.ews.local/qm$:p;
    /SXFILEWS001.ews.local/roh_dat$:r;
    /smuffile001/daten$:f;
    /smuffile001/qm$:p;
    /smuffile001/ROHDATEN$:r
    /spanfile001/daten$:f;
    /spanfile001/qm$:p;
    /smuffile001/ROHDATEN$:r
    """.strip().split("\n"),
    )
)


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


class FrozenModel(BaseModel):
    model_config = ConfigDict(frozen=True, strict=False, validate_default=True, defer_build=True)


class Paths(FrozenModel):
    mount_point: str = "/mnt"
    drives: str = "c;d;f;p;r"
    mappings: str = default_mappings


class SharePoint(FrozenModel):
    username: str = email
    password: str = ""
    site: str = "https://ewsconsulting.sharepoint.com/sites/teams_mb/"
    server: str = "ewsconsulting.sharepoint.com"


class GitHub(FrozenModel):
    username: str = gh_username
    token: str = ""


class EwsTools(FrozenModel):
    url: str = "https://mb.ews.tools"
    host: str = "smufcm.ews.local"
    port: int = 52812
    username: str = "mb_upload"
    password: str = ""


class AmmonitOR(FrozenModel):
    username: str = "wm@ews-consulting.com"
    password: str = ""


class WindCubeInsights(FrozenModel):
    username: str = "wm@ews-consulting.at"
    password: str = ""


class DevPi(FrozenModel):
    hostname: str = hostname
    port: int = 8051
    index: str = "root/private"
    url: str = r"root/all/+simple"


class PyServer(FrozenModel):
    hostname: str = ""
    port: int = 8050
    index: str = ""
    url: str = "simple"


class PyServers(FrozenModel):
    local: PyServer = Field(default_factory=lambda: PyServer(hostname=hostname))
    remote: PyServer = Field(default_factory=PyServer)


class DevPis(FrozenModel):
    local: DevPi = Field(default_factory=lambda: DevPi(hostname=hostname))
    remote: DevPi = Field(default_factory=DevPi)
