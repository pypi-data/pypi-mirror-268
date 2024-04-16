from __future__ import annotations

import platform
import sys
from importlib import metadata
from pathlib import Path

# Do not use the namespace package!!!
VERSION = metadata.version("ews-core-config")


def _get_sys_info() -> dict[str, str]:
    """System information

    Returns:
        system and Python version information
    """

    blob = [
        ("python", sys.version.replace("\n", " ")),
        ("executable", sys.executable),
        ("platform", platform.platform()),
    ]

    return dict(blob)


def _get_deps_info() -> dict[str, str]:
    """Overview of the installed version of main dependencies

    Returns:
        version information on relevant Python libraries
    """
    deps = [
        "ews-core-config",
        "pydantic",
        "tomlkit",
        "click",
    ]
    deps_info = {}

    for modname in deps:
        try:
            deps_info[modname] = metadata.version(modname)
        except ModuleNotFoundError:  # pragma: no cover
            deps_info[modname] = ""

    return deps_info


def show_versions() -> None:
    """
    Show the versions of the package with its optional dependencies

    Example:
        ```python
        import ews_core_config

        ews_core_config.show_versions()
        ```

    """
    sys_info: dict[str, str] = _get_sys_info()
    deps_info: dict[str, str] = _get_deps_info()

    maxlen = max(len(x) for x in sys_info)
    if deps_info:
        maxlen = max(maxlen, *(len(x) for x in deps_info))
    else:  # pragma: no cover
        pass
    maxlen += 2

    tpl: str = f"{{k:<{maxlen}}}: {{stat}}"
    print("\nSYSTEM INFO")
    print("-----------")
    for k, stat in sys_info.items():
        print(tpl.format(k=k, stat=stat))

    if deps_info:
        print("\nPYTHON DEPENDENCIES")
        print("-------------------")
        for k, stat in deps_info.items():
            print(tpl.format(k=k, stat=stat))


def version_info() -> str:
    """
    Show the version info

    Example:
        ```python
        import ews_core_config as ews_cfg

        print(ews_cfg.version_info())
        ```

    """
    sys_info: dict[str, str] = _get_sys_info()
    deps_info: dict[str, str] = _get_deps_info()
    optional_deps: list[str] = [f"{k}=={v}" for k, v in deps_info.items() if k]

    info = {
        "ews_core_config version": VERSION,
        "install path": Path(__file__).resolve().parent,
        "python": sys_info["python"],
        "platform": sys_info["platform"],
        "optional deps. installed": optional_deps,
    }
    return "\n".join("{:>30} {}".format(k + ":", str(v).replace("\n", " ")) for k, v in info.items())


__all__ = ("VERSION", "show_versions", "version_info")
