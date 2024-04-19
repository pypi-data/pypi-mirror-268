# pytest-dashboard

## usage
`python -m pytest`
by this command, you get `[datetime]-progress.yaml` file on working directory as realtime pytest progress report.

`python -m pytest --progress-path=[path/to/progress.yaml]`
by this command, you get `path/to/progress.yaml` file.

`python -m pytest_dashboard.tolly --progress-dir=[dir/contains/progress.yaml_files]`
by this command, you monitor -progress.yaml files
inside `dir/contains/progress.yaml_files`
and continurous update to tolly them
to `--entire-progress-path` (optional, default to `entire-progress.yaml`) file.

`python -m pytest_dashboard.launch_pytest_dashboard`
NOT IMPLEMENTED!
