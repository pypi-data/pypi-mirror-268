# To configure poetry virtual environment in vscode

```sh
poetry config virtualenvs.in-project true

poetry install
```

# To publish PYPI package

```sh
poetry config pypi-token.pypi <your api token>

poetry build

poetry publish
```
