from datetime import datetime # pylint: disable=unused-import
import json
import click as ck
from daily_tasks.commands import utilities


@ck.command
@ck.option(
    '-id', '--task-id',
    type=ck.INT,
    required=True
)
@ck.option(
    '-d', '--new-description',
    type=ck.STRING,
    required=False
)
@ck.option(
    '-p', '--new-priority',
    type=ck.Choice(utilities.PRIORITIES, case_sensitive=False),
    required=False
)
@ck.option(
    '-s', '--new-status',
    type=ck.Choice(utilities.STATUS, case_sensitive=False),
    required=False
)
@ck.option(
    '-dd', '--new-due-date',
    type=ck.DateTime(formats=utilities.DUE_DATE_FORMAT),
    required=False
)
def modify(task_id, new_description, new_priority, new_status, new_due_date):
    """Modify a task info."""
    with open(utilities.TASKS_FILE_PATH, 'r', encoding='utf-8') as tasks_file_read:
        tasks = json.load(tasks_file_read)

    for task in tasks:
        if task['id'] == task_id:
            extracted_task = task
            break

    task_index = tasks.index(extracted_task)

    if new_description:
        extracted_task['description'] = new_description.capitalize()

    if new_priority:
        new_priority_upper = new_priority.upper()
        extracted_task['priority'] = new_priority_upper

    if new_status:
        new_status_capitalize = new_status.capitalize()
        extracted_task['status'] = new_status_capitalize

    if new_due_date:
        new_due_date_date_object = new_due_date.date()
        new_due_date_formatted = new_due_date_date_object.strftime(utilities.DUE_DATE_FORMAT[0])

        extracted_task['due_date'] = new_due_date_formatted

    tasks.pop(task_index)
    tasks.insert(task_index, extracted_task)

    with open(utilities.TASKS_FILE_PATH, 'w', encoding='utf-8') as tasks_file_write:
        json.dump(tasks, tasks_file_write, indent=2)
