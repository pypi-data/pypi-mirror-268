from datetime import datetime # pylint: disable=unused-import
import json
import click as ck
from daily_tasks.commands import utilities


@ck.command
@ck.option(
    '-p', '--priority',
    type=ck.Choice(utilities.PRIORITIES, case_sensitive=False),
    required=False
)
@ck.option(
    '-s', '--status',
    type=ck.Choice(utilities.STATUS, case_sensitive=False),
    required=False
)
@ck.option(
    '-dd', '--due-date',
    type=ck.DateTime(formats=utilities.DUE_DATE_FORMAT),
    required=False
)
def filter_tasks(priority, status, due_date):
    """Filter tasks, use only one option for better results."""
    with open(utilities.TASKS_FILE_PATH, 'r', encoding='utf-8') as reading_tasks_file:
        tasks = json.load(reading_tasks_file)

    if priority:

        priority_upper = priority.upper()

        for task in tasks:
            if task['priority'] == priority_upper:

                task_id = task['id']
                task_description = task['description']
                task_priority = task['priority']
                task_due_date = task['due_date']
                task_status = task['status']

                utilities.stylized_tasks_printing(task_id, task_description, task_priority, task_due_date, task_status)

    if status:

        status_capitalize = status.capitalize()

        for task in tasks:
            if task['status'] == status_capitalize:

                task_id = task['id']
                task_description = task['description']
                task_priority = task['priority']
                task_due_date = task['due_date']
                task_status = task['status']

                utilities.stylized_tasks_printing(task_id, task_description, task_priority, task_due_date, task_status)

    if due_date:
        
        due_date_date_object = due_date.date()
        due_date_formatted = due_date_date_object.strftime(utilities.DUE_DATE_FORMAT[0])

        for task in tasks:
            if task['due_date'] == due_date_formatted:

                task_id = task['id']
                task_description = task['description']
                task_priority = task['priority']
                task_due_date = task['due_date']
                task_status = task['status']

                utilities.stylized_tasks_printing(task_id, task_description, task_priority, task_due_date, task_status)
