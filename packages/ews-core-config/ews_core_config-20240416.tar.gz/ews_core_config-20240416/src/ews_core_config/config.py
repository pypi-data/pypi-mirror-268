""" """

from __future__ import annotations

import logging
import os
from pathlib import Path

import tomlkit
from pydantic import Field
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)

import ews_core_config.schema as schema

log = logging.getLogger(__name__)

envs_prefix = os.getenv("EWS_ENVS_PREFIX", "EWS_")
config_path = os.getenv("EWS_CONFIG_PATH", Path.home() / ".config" / "ews")
config_file_name = os.getenv("EWS_CONFIG_FILENAME", "config")
if config_file_name.endswith(".toml"):
    config_file_name = config_file_name[:-4]

toml_file = Path(config_path) / f"{config_file_name}.toml"


class EWSSettings(BaseSettings, case_sensitive=False):
    paths: schema.Paths = Field(default_factory=schema.Paths)
    sharepoint: schema.SharePoint = Field(default_factory=schema.SharePoint)
    github: schema.GitHub = Field(default_factory=schema.GitHub)

    # Online documentation
    ewstools: schema.EwsTools = Field(default_factory=schema.EwsTools)

    # WEB Apis
    ammonitor: schema.WindCubeInsights = Field(default_factory=schema.WindCubeInsights)
    windcubeinsights: schema.WindCubeInsights = Field(default_factory=schema.WindCubeInsights)

    # Wheelhouse
    pyserver: dict[str, schema.PyServer] = Field(default_factory=lambda: schema.PyServers().model_dump())
    devpi: dict[str, schema.DevPi] = Field(default_factory=lambda: schema.DevPis().model_dump())

    model_config = SettingsConfigDict(
        toml_file=toml_file,
        extra="allow",
        env_prefix=envs_prefix,
        env_nested_delimiter="_",
        case_sensitive=False,
        frozen=True,
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (
            env_settings,
            dotenv_settings,
            TomlConfigSettingsSource(settings_cls),
            init_settings,
        )

    def create_env_vars(self) -> dict[str, str]:
        d = self.model_dump(mode="python")
        res = {}

        def make_env_var(value, parent_key=None) -> None:
            if isinstance(value, list):
                for i, val in enumerate(value):
                    k = (*parent_key, str(i)) if parent_key else (str(i),)
                    make_env_var(val, parent_key=k)
            elif isinstance(value, dict):
                for key, val in value.items():
                    k = (*parent_key, str(key)) if parent_key else (str(key),)
                    make_env_var(val, parent_key=k)
            else:
                res[parent_key] = str(value)

        make_env_var(d)
        r = {}
        env_prefix = self.model_config["env_prefix"]
        env_nested_delimiter = self.model_config["env_nested_delimiter"]
        for k, v in res.items():
            key = f"{env_prefix}{env_nested_delimiter.join(k)}"
            r[key.upper()] = v
        return r

    def export_env_vars(self) -> None:
        envs = self.create_env_vars()
        os.environ.update(envs)

    @property
    def toml_file(self) -> str:
        return str(self.model_config.get("toml_file", ""))

    def write_to_file(self, force: bool = False, **dumps_kws) -> None:
        out_file = self.model_config.get("toml_file", None)
        if not out_file:
            return
        out_file = Path(out_file)
        if out_file.is_file():
            if not force:
                raise RuntimeError(f"File {out_file!s} is not writable. Use force=True to allow")
        else:
            log.info(f"Creating {out_file!s}")
        data = tomlkit.dumps(self.model_dump(**dumps_kws))
        out_file.write_text(data)


def set_env_vars() -> None:
    EWSSettings().export_env_vars()


__all__ = ("set_env_vars", "EWSSettings")
