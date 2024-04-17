import os
from click.testing import CliRunner
import pytest
from daily_tasks.commands import filter_tasks
from daily_tasks.commands import export_tasks, modify, delete


def test_subtask_filtering():
    runner = CliRunner()

    priority = "H"
    due_date = "2024/03/15"
    status = "To-do"

    result = runner.invoke(filter_tasks, [
        '--priority', priority,
        '--due-date', due_date,
        '--status', status,
    ])
    assert result.exit_code == 0, f"Command failed: {result.exception}\n{result.output}"


@pytest.fixture()
def tmp_path(tmpdir):
    return tmpdir.strpath


def test_subtask_info(tmp_path):
    runner = CliRunner()
    test_file_path = os.path.abspath(os.getcwd())

    with runner.isolated_filesystem(temp_dir=tmp_path):
        result = runner.invoke(export_tasks, args=[
            '--export-path', test_file_path  # Pass the file path here
        ])

    assert result.exit_code == 0, f"Command failed:{result.exception}\n{result.output}"


def test_subtask_modify():
    runner = CliRunner()
    task_id = 2
    new_description = "Complete unit test sub commands modified"

    test_file_path = os.path.abspath(os.getcwd())
    result = runner.invoke(modify, [
        '--task-id', task_id,
        '--new-description', new_description,
    ])
    assert result.exit_code == 0, f"Command failed:{result.exception}\n{result.output}"


def test_subtask_delete():
    runner = CliRunner()
    task_id = 2
    result = runner.invoke(delete, [
        '--task-id', task_id,
    ])
    assert result.exit_code == 0, f"Command failed:{result.exception}\n{result.output}"
