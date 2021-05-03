import os


def test_only_one_backend(default_generated_project):
    file_in_docs = os.listdir('docs')
    assert "__sphinx" not in file_in_docs
    assert "__mkdocs" not in file_in_docs
    assert "conf.py" not in file_in_docs or "mkdocs.yml" not in file_in_docs
