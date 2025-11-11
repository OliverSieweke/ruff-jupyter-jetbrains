[![python](https://img.shields.io/badge/python-3.14-gray?style=for-the-badge&logo=python&logoColor=FFD43B&color=306998)](https://www.python.org/)
[![pypi](https://img.shields.io/pypi/v/ruff-jupyter-jetbrains?style=for-the-badge&logo=pypi&logoColor=f8d45f&color=306998)](https://pypi.org/project/ruff-jupyter-jetbrains/)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&style=for-the-badge)](https://docs.astral.sh/ruff/)
[![ty](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json&style=for-the-badge)](https://docs.astral.sh/ty/)
[![tests](https://img.shields.io/github/actions/workflow/status/OliverSieweke/ruff-jupyter-jetbrains/test.yml?style=for-the-badge&label=Tests&logo=github)](https://github.com/OliverSieweke/ruff-jupyter-jetbrains/actions/workflows/test.yml)


<br>

<!--suppress HtmlDeprecatedAttribute -->
<p align="center">
  <img width="20%" src="https://raw.githubusercontent.com/OliverSieweke/ruff-jupyter-jetbrains/main/assets/ruff.png" alt="Ruff Logo">
  <img width="20%" src="https://raw.githubusercontent.com/OliverSieweke/ruff-jupyter-jetbrains/main//assets/jetbrains.png" alt="Ruff Logo">
</p>


# ruff-jupyter-jetbrains

## Usage


---

## Development

### Setup

This project uses `uv` as a **project manager**. To set up the environment, ensure `uv` is [installed](https://docs.astral.sh/uv/getting-started/installation/) and run:

```shell
uv sync
```

To ensure code follows the project’s guidelines, install **pre-commit hooks** with:

```shell
pre-commit install
```

### **Code Standards**

`ruff` is used as a **formatter** and can be run with:

```shell
ruff format
```

`ruff` is used as a **linter** and code can be checked with:

```shell
ruff check
```

`ty` is used as a **type checker** and code can be checked with:

```shell
ty check
```
