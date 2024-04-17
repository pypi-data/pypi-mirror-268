import json
import click as ck
from daily_tasks.commands import utilities


@ck.command
@ck.option(
    '-id', '--task-id',
    type=ck.INT,
    required=False,
    help='Id of the task you want to delete.'
)
@ck.option(
    '--done',
    is_flag=True,
    required=False,
    help='Will delete all done tasks.'
)
def delete(task_id, done):
    """Delete tasks."""
    with open(utilities.TASKS_FILE_PATH, 'r', encoding='utf-8') as reading_tasks_file:
        tasks = json.load(reading_tasks_file)

    if task_id:
        for task in tasks:
            if task['id'] == task_id:
                task_index = tasks.index(task)
                tasks.pop(task_index)

    amount_of_tasks = len(tasks)

    for i in range(amount_of_tasks): # pylint: disable=unused-variable
        if done:
            for task in tasks:
                done_status = utilities.STATUS[2]

                if task['status'] == done_status:
                    task_index = tasks.index(task)
                    tasks.pop(task_index)

    with open(utilities.TASKS_FILE_PATH, 'w', encoding='utf-8') as writing_tasks_file:
        json.dump(tasks, writing_tasks_file, indent=2)
