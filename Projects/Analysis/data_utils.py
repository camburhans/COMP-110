"""Utility functions for wrangling data."""

__author__ = "730398410"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    rows: list[dict[str, str]] = []
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return rows


def column_values(table: list[dict[str, str]], subject_age: str) -> list[str]:
    """Producing names in the second parameter of a list."""
    column_values: list[str] = []
    for row in table:
        column_values.append(row[subject_age])
    return column_values


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Producing columns given a table represented as a list of rows."""
    dictionary: dict[str, list[str]] = {}
    for row in table:
        for key in row:
            dictionary[key] = column_values(table, key)
    return dictionary


def head(column_data: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Produce new column-based table with only the first N rows of data."""
    data_table: dict[str, list[str]] = {}
    for column in column_data:
        col_list: list[str] = column_data[column]
        x: int = 0
        row_val: list[str] = []
        while x < N:
            row_val.append(col_list[x])
            x += 1
        data_table[column] = [row_val]
    return data_table


def select(select_table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Produce new column-based table with only a specific subset of columns."""
    data_table: dict[str, list[str]] = {}
    for column in col_names:
        data_table[column] = select_table[column]
    return data_table


def count(list_values: list[str]) -> dict[str, int]:
    """Produce a dictionary where each key is a unique value."""
    common_values: dict[str, int] = {}
    for value in list_values:
        if value in common_values:
            common_values[value] += 1
        else:
            common_values[value] = 1
    return common_values


def list_mask(column: list[str], thresh: str) -> list[bool]:
    result: list[str] = []
    for value in column:
        result.append(value == thresh)
    return result


def list_masked(column: list[str], mask: list[bool]) -> list[str]:
    result: list[str] = []
    for x in range(len(mask)):
        if mask[x]:
            result.append(column[x])
    return result