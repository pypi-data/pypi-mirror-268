"""
Test suite for the module [ews_env.version](site:api/ews_env/version).
"""

from __future__ import annotations

import re

from packaging.version import (
    parse as parse_version,  # pyright: ignore [reportMissingImports]
)

import ews_core_config


def test_version_info():
    """Test the version_info"""
    s = ews_core_config.version_info()
    assert re.match(" *ews_core_config version: ", s)
    assert s.count("\n") == 4


def test_standard_version():
    """Test the standard version"""
    v = parse_version(ews_core_config.VERSION)
    assert str(v) == ews_core_config.VERSION


def test_version_attribute_is_present():
    """Test that __version__ is present"""
    assert hasattr(ews_core_config, "__version__")


def test_version_attribute_is_a_string():
    """Test that __version__ is a string"""
    assert isinstance(ews_core_config.__version__, str)
