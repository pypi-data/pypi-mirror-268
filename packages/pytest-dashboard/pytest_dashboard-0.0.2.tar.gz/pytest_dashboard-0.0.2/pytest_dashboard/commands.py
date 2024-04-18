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


def run_pytest(debug=False):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d',
        '--directory',
        help='test を含むディレクトリ',
        type=str
    )
    # parser.add_argument(
    #     "-c",
    #     "--csv-path",
    #     help="some optional argument",
    #     type=str
    # )

    args = parser.parse_args()

    if debug:
        directory = SAMPLE_DIRECTORY

    else:
        assert os.path.exists(args.directory)
        directory = args.directory

    result_path = os.path.join(directory, f'{datetime.datetime.now().strftime("%Y%m%d-%H%M%S")}-pytest-result.xml')

    # run pytest
    run([
        sys.executable,
        '-m',
        'pytest',
        # f'--junit-xml={result_path}',  # [options]
        '--capture=no',
        directory,
    ])


def launch_pytest_dashboard():
    ...


if __name__ == '__main__':
    run_pytest(debug=True)
    # _parse_junit()