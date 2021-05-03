import pytest
import subprocess
import sys
import os
import pathlib
import json
from cookiecutter.main import cookiecutter

_template_dir = pathlib.Path(__file__).parent.parent


@pytest.fixture(scope="session")
def default_generated_project(tmpdir_factory):
    cwd = os.getcwd()
    try:
        base_temp_dir = tmpdir_factory.mktemp("default_generated_project")
        os.chdir(base_temp_dir)
        subprocess.check_call(
            [
                sys.executable,
                "-m",
                "cookiecutter",
                "--no-input",
                str(_template_dir),
            ],
            stderr=subprocess.STDOUT,
        )
        os.chdir("my-python-package")
        yield os.getcwd()
    finally:
        os.chdir(cwd)
