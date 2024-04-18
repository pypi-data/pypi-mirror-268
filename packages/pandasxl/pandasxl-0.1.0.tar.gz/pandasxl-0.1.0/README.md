# pandasxl

pandasxl provides convenience functions for reading data from Excel files 
into a pandas DataFrame.

## Installation

...

## Usage

For example, to read a table from an Excel file into a DataFrame:

```python
import openpyxl
import pandasxl as pdxl

wb = openpyxl.load_workbook('file.xlsx')
df = pdxl.read.from_name(wb, 'table_name')
```

## API

Public API of the `pandasxl` package.

### Read

The `read` module contains the core functions for reading data from Excel files.

* `read.from_name(wb: openpyxl.Workbook, name: str, header: bool) -> pd.DataFrame`

Read an Excel named range or table into a DataFrame.

* `read.from_reference(wb: openpyxl.Workbook, ref: str) -> pd.DataFrame`

Read an Excel range reference into a DataFrame.

