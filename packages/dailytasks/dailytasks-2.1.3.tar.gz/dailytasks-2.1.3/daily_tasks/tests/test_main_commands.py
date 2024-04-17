from click.testing import CliRunner

from daily_tasks.commands.main_commands import view, add
from daily_tasks.commands.utilities import TASKS_FILE_NAME


def test_add_task():
    runner = CliRunner()

    description = "Complete unit test"
    priority = "H"
    due_date = "2024/03/15"
    status = "To-do"
    test_task_data_file = TASKS_FILE_NAME

    result = runner.invoke(add , [
        '--description', description,
        '--priority', priority,
        '--due-date', due_date,
        '--status', status,
        '--file-path', test_task_data_file,
    ])

    assert result.exit_code == 0, f"Command failed: {result.exception}\n{result.output}"


def test_view_tasks():
    runner = CliRunner()
    test_task_data_file = TASKS_FILE_NAME
    result = runner.invoke(view , ['--file-path', test_task_data_file])

    assert result.exit_code == 0, f"Command failed: {result.exception}\n{result.output}"
