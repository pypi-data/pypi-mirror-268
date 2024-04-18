from pathlib import Path

import rich
import typer
from pydantic_settings_toml.exceptions import TomlSettingsError

from ..api import SanetApi
from ..exceptions import SanetError
from ..schemas.models import Element
from ..settings import AppSettings, SanetSettings


def init_app_settings(env_file: Path | None = None) -> AppSettings:
    try:
        return AppSettings(_env_file=env_file)
    except TomlSettingsError as tse:
        raise SanetError(tse) from tse


def cli_init_setting(env_file: Path | None = None) -> AppSettings:
    try:
        return init_app_settings(env_file=env_file)
    except SanetError as ie:
        rich.print(f"[bold red]{ie}[/bold red]")
        raise typer.Exit(code=10) from ie


def cli_init_api(env_file: Path | None = None) -> tuple[SanetApi, AppSettings]:
    settings = cli_init_setting(env_file=env_file)
    try:
        api = SanetApi(settings=settings.pysanet)
        return api, settings
    except Exception as exc:
        rich.print(f"[bold red]{exc}[/bold red]")
        raise typer.Exit(code=11) from exc


def get_element_descripion(setting: SanetSettings, element: Element):
    if element.is_node():
        return (
            f"[magenta2][link={setting.portal_url}{element.absolute_url}]{element.name}"
            f"[/link][/magenta2]"
        )

    return (
        f"[magenta2][link={setting.portal_url}{element.absolute_parent_url}]{element.parent_name}"
        f"[/link][/magenta2]"
        f":[cyan1][link={setting.portal_url}{element.absolute_url}]{element.name}[/link][/cyan1]"
    )
