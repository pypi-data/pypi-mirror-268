"""Contains shared functionality used across multiple modules"""

import json
from typing import Union


def load_notebook_data(notebook_path: str) -> dict:  # pragma: no cover
    """Loads the notebook data from the given path

    Args:
        notebook_path: Path to the notebook file.

    Returns:
        dict: Notebook data in dictionary format.
    """
    with open(notebook_path, "r", encoding="UTF-8") as notebook_file:
        notebook_data = json.load(notebook_file)
    return notebook_data


def get_code_cells(notebook_data: dict) -> list:  # pragma: no cover
    """Returns a list of code cells from the notebook data

    Args:
        notebook_data: Notebook data in dictionary format.

    Returns:
        list: List of code cells.
    """
    code_cells = []
    for cell in notebook_data["cells"]:
        if cell["cell_type"] == "code":
            code_cells.append(cell)
    return code_cells


def parse_cell_comment(cell: dict) -> Union[str, None]:
    """Returns the comment from the first line of the cell, if present

    Args:
        cell: The cell to parse

    Returns:
        str: The comment from the first line of the cell, if present
    """
    first_line = cell["source"][0]
    if first_line.startswith("#"):
        return first_line[1:].strip()
    return None


def cell_has_no_run_comment(cell_data: dict):
    """Returns True if the cell has a no-run comment

    Args:
        cell_data: The cell to check

    Returns:
        bool: True if the cell has a no-run comment
    """

    comment = parse_cell_comment(cell_data)
    if comment is None:
        return False
    return comment.lower() == "no-run"


def cell_has_no_check_output_comment(cell_data: dict):
    """Returns True if the cell has a no-check-output comment

    Args:
        cell_data: The cell to check

    Returns:
        bool: True if the cell has a no-check-output comment
    """
    comment = parse_cell_comment(cell_data)
    if comment is None:
        return False
    return comment.lower() == "no-check-output"
