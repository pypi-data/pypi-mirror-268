# DailyTasks #
A tasks manager for those who like work from shell.

![PyPI - Version](https://img.shields.io/pypi/v/dailytasks?style=for-the-badge&label=Lastest%20version&color=008B8B&link=https%3A%2F%2Fpypi.org%2Fproject%2Fdailytasks%2F)
![GitHub issue custom search in repo](https://img.shields.io/github/issues-search/LuisanaMTDev/dailytasks?query=is%3Aopen&style=for-the-badge&label=Open%20issues&color=008B8B&link=https%3A%2F%2Fgithub.com%2FLuisanaMTDev%2Fdailytasks%2Fissues%3Fq%3Dis%253Aissue%2Bis%253Aopen)

## Installation ##
**Requirements:**
- Python >= 3.11

**How install it:**

`pip install dailytasks`

## Update process ##
1. Before update this package execute `dailytasks export` command to save all your data.

    1.1. Provide a path to the command (with `-p` option) is required for it execution, this path is where your data will be saved.

    1.2. This command will create a json file named 'exported_tasks' in the path provided path.

2. After update execute `dailytasks import` command to restore all your data.

    2.1. Provide the path provided before (with `-p` option) and all your data will be restore.

   **This is because when you update the CLI, data folder ([data_files](./daily_tasks/data_files/)) is overwritten and all your data deleted.**
   
## Testing ##

Running tests locally:

1. Clone this repository.

1. cd into your clone.

2. Use `pytest test` to run all tests, use `pytest test/test_file_name` to run individual tests.
   
3. If you get errors around missing daily_task module, reinstall package using `pip install dailytasks`.

## Contributing ##
Read [Contributing file](https://github.com/LuisanaMT2005/dailytasks/blob/main/CONTRIBUTING.md) and make whatever question in Discussions.

### Thanks to: ###
[Krishnag09](https://github.com/Krishnag09) for contributing closing [#2](https://github.com/LuisanaMTDev/dailytasks/issues/2) and [#8](https://github.com/LuisanaMTDev/dailytasks/issues/8) issues.
