import pathlib
import subprocess


def test_pyproject_toml(default_generated_project):
    subprocess.check_call(["poetry", "check"])


def test_tox(tmp_generated_project: pathlib.Path):
    subprocess.check_call(["tox"])


def test_pre_commit(tmp_generated_project: pathlib.Path):
    subprocess.check_call(["git", "init"])
    subprocess.check_call(["pre-commit", "install"])
    subprocess.check_call(["pre-commit", "run", "--all"])


def test_build_wheel(tmp_generated_project: pathlib.Path):
    subprocess.check_call(["poetry", "build"])
