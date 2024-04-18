"""Create and update [datetime]-progress.yaml file as processing progresses.

YAML basic format

key01: value01  # yaml['key01'] == 'value01'
key02: 1  # yaml['key02'] == 1
key03: true  # yaml['key03'] == True
key04: null  # yaml['key04'] is None

# yaml['list'][0] == 'element01'
list:
  - element01
  - element02
  - element03

"""


import os
import datetime
# from typing import Tuple

from pytest import (
    Session,
    # Config,
    TestReport,
)


BR = '\n'
during_test = False
progress_path = None


def set_log_path(root):
    global progress_path
    progress_path = os.path.join(
        root,
        datetime.datetime.now().strftime('%Y%m%d-%H%M%S-progress.yaml'),
    )


def pytest_collection_finish(session: Session):
    set_log_path(session.startpath)  # directory where pytest is launched
    # file_or_dir: Tuple[str] or None = session.config.getoption('file_or_dir'))  # list of specified [file_or_dir]
    with open(progress_path, 'w', encoding='utf-8', newline=BR) as f:
        f.write(f'items:{BR}')
        f.writelines([f'  - {item.name}{BR}' for item in session.items])
        f.write(f'results:{BR}')


def pytest_runtest_setup(item):
    global during_test
    during_test = True
    with open(progress_path, 'a', encoding='utf-8', newline=BR) as f:
        f.write(f'  -{BR}')
        f.write(
            f'    name: {item.name}{BR}'
        )


def pytest_report_teststatus(report: TestReport, config):
    global during_test
    if during_test:
        with open(progress_path, 'a', encoding='utf-8', newline=BR) as f:
            f.write(
                f'    {report.when}: {report.outcome}{BR}'
            )
    if report.when == 'teardown':
        during_test = False


def pytest_runtest_teardown(item):
    # global during_test
    # during_test = False
    pass
