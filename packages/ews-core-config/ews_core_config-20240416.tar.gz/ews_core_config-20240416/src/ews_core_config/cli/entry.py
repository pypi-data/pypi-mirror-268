from __future__ import annotations

import io
from pathlib import Path
from pprint import pprint

import click

from ews_core_config.config import EWSSettings
from ews_core_config.version import VERSION


@click.group()
@click.version_option(VERSION, "-v", "--version", is_flag=True, help="Show the version")
def cli():
    pass


def show_dict_as_env(d: dict, export: bool = False, **kwargs):
    if not d:
        return
    p = "export " if export else ""
    for k, v in d.items():
        txt = f'{p}{k.upper()}="{v}"'
        click.secho(txt, **kwargs)


def show_dict_as_text(d: dict, min_pad: int = 20, **kwargs):
    if not d:
        return
    max_pad = max(map(len, d.keys())) + 3
    max_pad = max(min_pad, max_pad)
    for k, v in d.items():
        txt = f"{k.ljust(max_pad)}: {v}"
        click.secho(txt, **kwargs)


def pprint_dict(d: dict, **kwargs):
    if not d:
        return
    stream = io.StringIO()
    pprint(d, stream=stream)
    stream = stream.getvalue()
    click.secho(stream, **kwargs)


@cli.command(name="show", help="Show the config attributes and values")
@click.option("-t/-nt", "--text/--no-text", is_flag=True, default=True, show_default=True)
@click.option("-l/-nl", "--location/--no-location", is_flag=True, default=True, show_default=True)
def show(text: bool = True, location: bool = True):
    settings = EWSSettings()
    cfg_filename = Path(settings.toml_file)
    if location:
        click.secho(f"Location: {cfg_filename!s}\n", fg="yellow", bold=True)

    nice = settings.model_dump(mode="python")
    if text:
        show_dict_as_text(nice, fg="blue")
    else:
        pprint_dict(nice, fg="blue")


@cli.command(name="env", help="Show the set environment variables")
@click.option("-t/-nt", "--text/--no-text", is_flag=True, default=True, show_default=True)
@click.option("-e/-ne", "--env/--no-env", is_flag=True, default=False, show_default=True)
@click.option("--export", is_flag=True, default=False, show_default=True)
@click.option("-l/-nl", "--location/--no-location", is_flag=True, default=True, show_default=True)
def env(text: bool = True, env: bool = False, export: bool = False, location: bool = True):
    settings = EWSSettings()

    if env or export:
        text = location = False
        env = True

    cfg_filename = Path(settings.toml_file)
    if location:
        click.secho(f"Location: {cfg_filename!s}\n", fg="yellow", bold=True)
    env_vars = settings.create_env_vars()
    if text:
        show_dict_as_text(env_vars, fg="blue")
    elif env:
        show_dict_as_env(env_vars, export=export, fg="blue")
    else:
        pprint_dict(env_vars, fg="blue")


@cli.command(name="path", help="Show the path of the config file")
def _path() -> None:
    settings = EWSSettings()
    cfg_filename = Path(settings.toml_file)
    click.echo(f"{cfg_filename!s}")


@cli.command(name="init", help="Create a new config file if it does not exist")
@click.option("--verbose/--quiet", is_flag=True, default=True, show_default=True)
def _init(verbose: bool) -> None:
    settings = EWSSettings()
    settings.write_to_file(force=False, mode="python")
    cfg_filename = Path(settings.toml_file)
    if verbose:
        click.echo(f"Created {cfg_filename!s}")


@cli.command(name="update", help="Update a config file if it does not exist")
@click.option("--verbose/--quiet", is_flag=True, default=False, show_default=True)
def _update(verbose: bool) -> None:
    settings = EWSSettings()
    cfg_filename = Path(settings.toml_file)
    settings.write_to_file(force=True)
    if verbose:
        click.echo(f"{cfg_filename!s}")
