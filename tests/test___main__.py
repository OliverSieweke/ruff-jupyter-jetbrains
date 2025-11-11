import subprocess
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "notebook_file_name,expected_output_file_name,expected_returncode",
    [
        ("single_code_cell.ipynb", "single_code_cell_expected_output.txt", 1),
        ("several_code_cells.ipynb", "several_code_cells_expected_output.txt", 1),
        ("with_markdown_cells.ipynb", "with_markdown_cells_expected_output.txt", 1),
        ("empty.ipynb", "empty_expected_output.txt", 0),
        ("no_linting_errors.ipynb", "no_linting_errors_expected_output.txt", 0),
        ("only_markdown_cells.ipynb", "only_markdown_cells_expected_output.txt", 0),
    ],
)
def test_notebook_linting_output(
    notebook_file_name, expected_output_file_name, expected_returncode
):
    expected_output_content = (
        (Path("tests/fixtures") / expected_output_file_name).read_text().strip()
    )

    result = subprocess.run(
        [
            "uv",
            "run",
            "ruff-jupyter-jetbrains",
            Path("tests/fixtures") / notebook_file_name,
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == expected_returncode
    assert result.stderr == ""
    assert result.stdout == expected_output_content


def test_rejects_non_ipynb_files():
    result = subprocess.run(
        [
            "uv",
            "run",
            "ruff-jupyter-jetbrains",
            Path("tests/fixtures") / "bad_extension.ipnb",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 2
    assert (
        result.stderr
        == "\x1b[91mruff-jupyter-jetbrains is designed to be run on \x1b[4m.ipynb\x1b[24m files. Make sure the JetBrains file watcher is configured for Jupyter files exclusively.\x1b[0m\n"
    )
    assert result.stdout == ""


def test_requires_at_leat_one_file_path_arguments():
    result = subprocess.run(
        [
            "uv",
            "run",
            "ruff-jupyter-jetbrains",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 2
    assert (
        result.stderr
        == "\x1b[91mNo file specified. Make sure you provide the JetBrains $FilePath$ argument in the file watcher run configurations\x1b[0m\n"
    )
    assert result.stdout == ""


def test_requires_at_most_one_file_path_arguments():
    result = subprocess.run(
        [
            "uv",
            "run",
            "ruff-jupyter-jetbrains",
            Path("tests/fixtures") / "single_code_cell.ipnb",
            Path("tests/fixtures") / "several_code_cells.ipnb",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 2
    assert (
        result.stderr
        == "\x1b[91mSeveral files specified. Make sure you only provide the JetBrains $FilePath$ argument in the file watcher run configurations\x1b[0m\n"
    )
    assert result.stdout == ""


def test_nonexistent_ipynb_file():
    result = subprocess.run(
        [
            "uv",
            "run",
            "ruff-jupyter-jetbrains",
            Path("tests/fixtures") / "non_existing.ipynb",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 2
    assert (
        result.stderr
        == "\x1b[91mFile tests/fixtures/non_existing.ipynb does not exist. This is unexpected if you use ruff-jupyter-jetbrains as a file watcher.\x1b[0m\n"
    )
    assert result.stdout == ""
