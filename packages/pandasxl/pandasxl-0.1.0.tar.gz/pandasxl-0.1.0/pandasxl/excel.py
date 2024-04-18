"""Utility functions for working with Excel files."""

import io
import re
from pathlib import Path
from typing import Any

import numpy as np
import openpyxl
from numpy import dtype, ndarray
from openpyxl import Workbook

SHEET_RANGE_PATTERN = re.compile(
    r"(('(?P<quoted>([^']|'')*)')|(?P<notquoted>[^'^ ^!]*))!(?P<cells>[$]?(?P<min_col>[A-Za-z]{1,3})[$]?(?P<min_row>\d+)?(:[$]?(?P<max_col>[A-Za-z]{1,3})?[$]?(?P<max_row>\d+)?)?)(?=,?)"
)


def open_workbook(xlsx_file: Path, data_only: bool = False) -> Workbook:
    """Open an Excel workbook from a file.

    Parameters
    ----------
    xlsx_file: Path
        Path to the Excel file to open.
    data_only: bool, default False
        Whether to load the cached values of cells.

    Returns
    -------
    Workbook
        The opened workbook.
    """
    with open(xlsx_file, "rb") as f:
        in_mem_file = io.BytesIO(f.read())
    return openpyxl.load_workbook(in_mem_file, read_only=False, data_only=data_only)


def named_ranges(workbook: Workbook) -> dict[str, tuple[str, str]]:
    """Return a dictionary of named ranges in the workbook.

    A named range is a defined name that refers to a range of cells on a worksheet.

    Parameters
    ----------
    workbook: Workbook
        The workbook to extract named ranges from.

    Returns
    -------
    dict[str, tuple[str, str]]
        A dictionary of range names and their corresponding worksheet and cell range.
    """
    return {
        # TODO: Handle multiple destinations for non-contiguous ranges
        defined_name.name: next(iter(defined_name.destinations))
        for _, defined_name in workbook.defined_names.items()
        if SHEET_RANGE_PATTERN.match(defined_name.value)
    }


def table_ranges(workbook: Workbook) -> dict[str, tuple[str, str]]:
    """Return a dictionary of tables in the workbook.

    A table is a structured range of data that is managed by Excel.

    Parameters
    ----------
    workbook: Workbook
        The workbook to extract tables from.

    Returns
    -------
    dict[str, tuple[str, str]]
        A dictionary of table names and their corresponding worksheet and cell range.
    """
    return {t.name: (ws.title, t.ref) for ws in workbook for t in ws.tables.values()}


def range_to_array(
    excel_range: tuple[str, str], workbook: Workbook
) -> ndarray[Any, dtype[Any]]:
    """Return a 2d array of Cells from a workbook.

    Parameters
    ----------
    excel_range: tuple[str, str]
        Worksheet and cell reference to extract.
    workbook: Workbook
        Workbook containing the cell range.

    Returns
    -------
    tuple[tuple[Cell], ...]
        A matrix of Cells from the cell range.
    """
    worksheet, ref = excel_range
    cells = workbook[worksheet][ref]
    if not isinstance(cells, tuple):
        return np.array(((cells,),))
    return np.array(cells)


def reference_to_array(reference: str, workbook: Workbook) -> ndarray[Any, dtype[Any]]:
    """Return a 2d array of Cells from a qualified cell reference.

    Parameters
    ----------
    reference: str
        Reference to the cell range.
    workbook: Workbook
        Workbook containing the cell range.

    Returns
    -------
    tuple[tuple[Cell], ...]
        A matrix of Cells from the cell range.
    """
    worksheet, ref = reference.split("!")
    cells = workbook[worksheet][ref]
    if not isinstance(cells, tuple):
        return np.array(((cells,),))
    return np.array(cells)
