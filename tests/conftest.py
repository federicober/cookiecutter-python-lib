import contextlib
import os
import pathlib
import shutil
import subprocess
import sys

import pytest
from cookiecutter.main import cookiecutter

_template_dir = pathlib.Path(__file__).parent.parent
_base_cookiecutter_args = {
    "project_name": "my-python-package",
    "package_name": "my_python_package",
    "friendly_name": "My Python Package",
    "author": "Federico OBERNDORFER",
    "email": "federico.ober@hotmail.com",
    "github_user": "federicober",
    "version": "0.1.0",
    "dockerized": "false",
    "docs_backend": "sphinx",
}


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


@pytest.fixture()
def custom_generated_project(tmp_path, request):
    cookiecutter_args = _base_cookiecutter_args.copy()
    if hasattr(request, "param"):
        cookiecutter_args.update(request.param)
    cookiecutter(
        str(_template_dir),
        output_dir=str(tmp_path),
        no_input=True,
        extra_context=cookiecutter_args,
    )
    project_dir = tmp_path / cookiecutter_args["project_name"]
    with change_dir(project_dir):
        yield project_dir
