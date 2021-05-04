# Cookiecutter Python library

Cookiecutter Python Library is a complete Python library template that contains support for:
- Packaging
- Testing
- Linting
- Documentation
- Pre-commit hooks
- And more ...

## Usage

Cookiecutter Python Library is used via [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/).
To install Cookiecutter:

```shell
pip install cookiecutter
```

Then use Cookiecutter to create your project:
```shell
cookiecutter https://github.com/federicober/cookiecutter-python-lib
```

You will be prompted for all relevant information by Cookiecutter.

## Development
To "install" in development mode and run the tests:

1. You will need [`tox`](https://tox.readthedocs.io/en/latest/) and [`poetry`](https://python-poetry.org/) installed in your machine ([`pre-commit`](https://pre-commit.com/) is also recommended).
```shell
pip install tox poetry pre-commit
```

2. Git clone the repository
```shell
git clone git@github.com:federicober/cookiecutter-python-lib.git
cd cookiecutter-python-lib
```

3. Install the development requirements and run the tests:
```shell
pip install -r requirements-dev.txt
pytest tests
```

4. (Optional) Install the git hooks using [`pre-commit`](https://pre-commit.com/):
```shell
pre-commit install
```


## Acknowledgements
[Hypermodern Python](https://github.com/cjolowicz/cookiecutter-hypermodern-python) by Claudio Jolowicz
for providing me with great inspiration and examples.
