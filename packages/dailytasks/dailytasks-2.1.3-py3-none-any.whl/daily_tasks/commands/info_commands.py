from os.path import join
import json
import click as ck
from daily_tasks.commands import utilities


@ck.command
@ck.option(
    '-p', '--export-path',
    type=ck.Path(exists=True, dir_okay=True, resolve_path=True),
    required=True
)
def export_tasks(export_path):
    """Export your tasks."""

    with open(utilities.TASKS_FILE_PATH, 'r', encoding='utf-8') as tasks_file:
        tasks = json.load(tasks_file)

    with open(join(export_path, utilities.EXPORTED_TASKS_FILE), 'w', encoding='utf-8') as exported_tasks_file:
        json.dump(tasks, exported_tasks_file, indent=2) 

@ck.command
@ck.option(
    '-p', '--import-path',
    type=ck.Path(exists=True, dir_okay=True, resolve_path=True),
    required=True,
    help=f'Directory/Folder where your {utilities.EXPORTED_TASKS_FILE} is.'
)
def import_tasks(import_path):
    """Import your tasks."""

    with open(join(import_path, utilities.EXPORTED_TASKS_FILE), 'r', encoding='utf-8') as imported_tasks_file:
        tasks = json.load(imported_tasks_file)

    with open(utilities.TASKS_FILE_PATH, 'w', encoding='utf-8') as tasks_file:
        json.dump(tasks, tasks_file, indent=2)
