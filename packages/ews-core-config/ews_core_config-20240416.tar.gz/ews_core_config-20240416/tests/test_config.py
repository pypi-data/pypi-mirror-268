from __future__ import annotations

import os

from ews_core_config.config import EWSSettings


def test_config() -> None:
    old_prefix = EWSSettings.model_config["env_prefix"]
    try:
        EWSSettings.model_config.update(env_prefix="XYZ_")
        settings = EWSSettings()
        settings.export_env_vars()
        envs = {k: v for k, v in os.environ.items() if k.startswith("XYZ_")}
        assert envs

    finally:
        EWSSettings.model_config.update(env_prefix=old_prefix)


def test_user_file_read():
    settings = EWSSettings()
    assert settings.sharepoint.username != ""
