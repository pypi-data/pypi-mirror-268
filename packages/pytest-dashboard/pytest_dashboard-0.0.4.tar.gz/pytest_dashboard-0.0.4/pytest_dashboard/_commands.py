import os
import sys
from subprocess import run
import argparse
import datetime


SAMPLE_DIRECTORY = os.path.join(
    os.path.dirname(__file__),
    '..',
    'sample-tests'
)


def run_pytest():  # debug code
    directory = SAMPLE_DIRECTORY

    # run pytest
    run([
        sys.executable,
        '-m',
        'pytest',
        '--capture=no',
        directory,
        # f'--progress-path={}'
    ])


if __name__ == '__main__':
    run_pytest(debug=True)
