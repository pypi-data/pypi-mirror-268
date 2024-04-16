from __future__ import annotations

import os

from ews_core_config.config import read_settings


def test_config():
    settings = read_settings(create_if_inexistent=True).get_settings()
    envs = {k: v for k, v in os.environ.items() if k.startswith("EWS_")}
    assert envs


def test_user_file_read():
    settings = read_settings(create_if_inexistent=True)
    assert settings.sharepoint_username != ""
