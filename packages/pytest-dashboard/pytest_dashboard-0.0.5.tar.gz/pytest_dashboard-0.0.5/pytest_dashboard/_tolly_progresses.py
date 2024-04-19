import os
from glob import glob
from time import sleep
from threading import Thread

import yaml

import pytest_dashboard


SAMPLE_PROGRESS_DIR = os.path.join(
    os.path.dirname(pytest_dashboard.__file__),
    '..',
    'sample-progress'
)

UPDATE_INTERVAL = 1

should_stop = False


def _progress_passed(data):
    # if empty, return False
    if data is None:
        return False

    # if all(results), return True
    passed_list = []
    for result in data['results']:
        name = result['name']
        setup = result['setup'] if 'setup' in result.keys() else None
        call = result['call'] if 'call' in result.keys() else None
        teardown = result['teardown'] if 'teardown' in result.keys() else None
        passed = True
        if setup is not None:

            passed = passed * (setup == 'passed')
        if call is not None:
            passed = passed * (call == 'passed')
        if teardown is not None:
            passed = passed * (teardown == 'passed')
        passed_list.append(passed)
    return all(passed_list)


def _progress_state(data):
    # if empty, not started
    if data is None:
        return 'not started'

    # if len(items) > len(results), in progress
    if len(data['items']) > len(data['results']):
        return 'in progress'

    # if len(items) == len(results), finished
    if len(data['items']) == len(data['results']):
        return 'finished'

    return 'undefined'


def merge_progress_files(progresses_dir, entire_progress_path):
    # glob all .yaml and check their state and passed
    merged_data = {}
    for path in glob(os.path.join(progresses_dir, '*progress.yaml')):
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
            name = os.path.basename(path)[:-14]  # -progress.yaml is 14 chars
            state = _progress_state(data)
            passed = _progress_passed(data)
            merged_data[name] = dict(state=state, passed=passed)

    # save merged entire-progress.yaml
    with open(entire_progress_path, 'w') as f:
        yaml.dump(merged_data, f)


def _update_forever(progresses_dir, entire_progress_path):
    while not should_stop:
        merge_progress_files(progresses_dir, entire_progress_path)
        sleep(UPDATE_INTERVAL)


def monitor_progress(progresses_dir, entire_progress_path=None):
    global should_stop

    if entire_progress_path is None:
        entire_progress_path = 'entire-progress.yaml'
    entire_progress_path = os.path.abspath(entire_progress_path)

    t = Thread(
        target=_update_forever,
        args=(progresses_dir, entire_progress_path,),
        daemon=True
    )
    t.start()
    print()
    print('##############')
    print(f'  Starts continuous update of {entire_progress_path}.')
    print('  Press enter to quit.')
    print('##############')
    input()
    should_stop = True


if __name__ == '__main__':
    monitor_progress(
        progresses_dir=SAMPLE_PROGRESS_DIR,
        entire_progress_path='entire.yaml'
    )

