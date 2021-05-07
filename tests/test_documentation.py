import os
import subprocess

import pytest


def test_only_one_backend(default_generated_project):
    files_in_docs = os.listdir("docs")
    assert "__sphinx" not in files_in_docs
    assert "__mkdocs" not in files_in_docs
    assert "conf.py" not in files_in_docs or "mkdocs.yml" not in files_in_docs


@pytest.mark.parametrize(
    "custom_generated_project", [{"docs_backend": "mkdocs"}], indirect=True
)
def test_mkdocs_backend(custom_generated_project):
    files_in_docs = os.listdir("docs")
    assert "__sphinx" not in files_in_docs
    assert "__mkdocs" not in files_in_docs
    assert "conf.py" not in files_in_docs

    assert "mkdocs.yml" in files_in_docs
    assert "docs" in files_in_docs
    md_files = os.listdir("docs/docs")
    assert "index.md" in md_files

    subprocess.check_call(["mkdocs", "build", "--strict", "-f", "docs/mkdocs.yml"])
