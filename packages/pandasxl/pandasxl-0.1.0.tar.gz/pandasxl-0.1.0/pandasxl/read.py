"""Read data from Excel into a DataFrame."""

import numpy as np
import openpyxl
import pandas as pd

from pandasxl import excel
from pandasxl.excel import reference_to_array


def from_name(
    workbook: openpyxl.Workbook, range_name: str, header: bool | None = None
) -> pd.DataFrame | pd.Series | str:
    """Read an Excel named range or table into a DataFrame.

    Parameters
    ----------
    workbook: openpyxl.Workbook
        Workbook to read from.
    range_name: str
        Name of the range or table read.
    header: bool, default None


    Returns
    -------
    pd.DataFrame | pd.Series | str
        DataFrame containing the data from the specified range.
    """
    names = excel.named_ranges(workbook)
    tables = excel.table_ranges(workbook)
    excel_range = {**names, **tables}[range_name]
    if range_name in tables:
        header = True
    cells = excel.range_to_array(excel_range, workbook)
    return _cells_to_pandas(cells, header)


def from_reference(
    workbook: openpyxl.Workbook, cell_reference: str
) -> pd.DataFrame | pd.Series | str:
    """Get a single rectangular region from the specified cell reference.

    Parameters
    ----------
    workbook: openpyxl.Workbook
        Workbook to read from.
    cell_reference: str
        Cell reference to read in.

    Returns
    -------
    pd.DataFrame
        DataFrame containing the data from the specified reference.
    """
    cells = reference_to_array(cell_reference, workbook)
    return _cells_to_pandas(cells)


def _cells_to_pandas(
    cell_array: np.ndarray, header: bool | None = None
) -> pd.DataFrame | pd.Series | str:
    """Convert an array of cells to a pandas object."""
    data = np.vectorize(lambda x: x.value)(cell_array)
    if data.shape == (1, 1):
        return _array_to_scalar(data)
    if 1 in data.shape:
        return _array_to_series(data, header)
    return _array_to_dataframe(data, header)


def _array_to_scalar(data: np.ndarray) -> str:
    """Convert a 1x1 array to a scalar value."""
    return str(data[0, 0])


def _array_to_series(data: np.ndarray, name: bool | None = None) -> pd.Series:
    """Convert a 1xN or Nx1 array to a Series."""
    data = data.flatten()
    if name:
        name = data[0]
        data = data[1:]
    return pd.Series(data, name=name)


def _array_to_dataframe(data: np.ndarray, header: bool | None = None) -> pd.DataFrame:
    """Convert a 2D array to a DataFrame."""
    if header:
        header = data[0, :]
        data = data[1:, :]
    return pd.DataFrame(data, columns=header)
