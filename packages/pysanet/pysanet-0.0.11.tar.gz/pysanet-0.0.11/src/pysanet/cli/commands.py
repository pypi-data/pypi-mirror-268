from pathlib import Path
from zoneinfo import ZoneInfo

import rich  # noqa
import typer
from devtools import debug  # noqa
from rich.progress import Progress
from rich.table import Table

from .utils import cli_init_api, get_element_descripion

app = typer.Typer()
nodes_app = typer.Typer()
app.add_typer(nodes_app, name="nodes")
alarms_app = typer.Typer()
app.add_typer(alarms_app, name="alarms")

state = {"env_file": None}


@app.callback()
def set_env_file(
    env_file: Path = typer.Option(  # noqa: B008
        Path("~/.pynta.toml"), "--env", "-e", help="Environment file in formato toml"
    ),
):
    state["env_file"] = env_file


@alarms_app.command("list")
def list_alarms(
    node_name: str = typer.Option("", "--node-name", "-n"),  # noqa: B008
):
    api, _ = cli_init_api(env_file=state["env_file"])
    node_name = node_name.lower()

    with Progress() as progress:
        task = progress.add_task("Get data from Sanet...", total=None)
        alarms = api.read_all_alarms()
        progress.remove_task(task)

    if len(alarms) == 0:
        typer.Exit("...")

    table = Table("Element", "Condition", "Priority", "Last Change", show_lines=True)

    if node_name:
        alarms = [alarm for alarm in alarms if node_name in alarm.element.path.lower()]

    for alarm in alarms:
        table.add_row(
            get_element_descripion(setting=api.settings, element=alarm.element),
            alarm.condition.description,
            alarm.condition.priority_level,
            alarm.condition.statuslastchange.astimezone(
                tz=ZoneInfo("Europe/Rome")
            ).strftime("%Y-%m-%d %H:%M"),
        )
    rich.print(table)
