import pytest
import subprocess
import contextlib
import sys
import os
import pathlib
import shutil

_template_dir = pathlib.Path(__file__).parent.parent


@contextlib.contextmanager
def change_dir(dir_name):
    cwd = os.getcwd()
    try:
        os.chdir(dir_name)
        yield
    finally:
        os.chdir(cwd)


@pytest.fixture(scope="session")
def default_generated_project(tmpdir_factory):
    base_temp_dir = tmpdir_factory.mktemp("default_generated_project")
    subprocess.check_call(
        [
            sys.executable,
            "-m",
            "cookiecutter",
            "--no-input",
            "--output-dir",
            str(base_temp_dir),
            str(_template_dir),
        ],
        stderr=subprocess.STDOUT,
    )
    project_dir = base_temp_dir / "my-python-package"
    with change_dir(project_dir):
        yield project_dir


@pytest.fixture()
def tmp_generated_project(default_generated_project, tmp_path):
    shutil.copytree(default_generated_project, tmp_path, dirs_exist_ok=True)
    with change_dir(tmp_path):
        yield tmp_path
