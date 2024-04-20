r"""Contain utility functions to manage data types."""

from __future__ import annotations

__all__ = [
    "frame_column_types",
    "find_date_columns_from_dtypes",
    "find_numeric_columns_from_dtypes",
    "get_dtypes_from_schema",
    "series_column_types",
]

import logging
from typing import TYPE_CHECKING

import pyarrow as pa

if TYPE_CHECKING:

    from pandas import DataFrame, Series

logger = logging.getLogger(__name__)


def frame_column_types(frame: DataFrame) -> dict[str, set]:
    r"""Return the value types per column.

    Args:
        frame: The DataFrame to analyze.

    Returns:
        A dictionary with the value types for each column.

    Example usage:

    ```pycon
    >>> import numpy as np
    >>> import pandas as pd
    >>> from flamme.utils.dtype import frame_column_types
    >>> frame = pd.DataFrame(
    ...     {
    ...         "int": np.array([np.nan, 1, 0, 1]),
    ...         "float": np.array([1.2, 4.2, np.nan, 2.2]),
    ...     }
    ... )
    >>> coltypes = frame_column_types(frame)
    >>> coltypes
    {'int': {<class 'float'>}, 'float': {<class 'float'>}}

    ```
    """
    types = {}
    for col in frame:
        types[col] = series_column_types(frame[col])
    return types


def series_column_types(series: Series) -> set[type]:
    r"""Return the value types in a ``pandas.Series``.

    Args:
        series: The DataFrame to analyze.

    Returns:
        A dictionary with the value types for each column.

    Example usage:

    ```pycon
    >>> import numpy as np
    >>> import pandas as pd
    >>> from flamme.utils.dtype import series_column_types
    >>> coltypes = series_column_types(pd.Series([1.2, 4.2, np.nan, 2.2]))
    >>> coltypes
    {<class 'float'>}

    ```
    """
    return {type(x) for x in series.tolist()}


def find_numeric_columns_from_dtypes(dtypes: dict[str, pa.DataType]) -> list[str]:
    r"""Find the columns with a numeric type.

    Args:
        dtypes: The mapping of column names and data types.

    Returns:
        The columns with a numeric type.
    """
    columns = []
    for col, dtype in dtypes.items():
        if pa.types.is_decimal(dtype) or pa.types.is_floating(dtype) or pa.types.is_integer(dtype):
            columns.append(col)
    return columns


def find_date_columns_from_dtypes(dtypes: dict[str, pa.DataType]) -> list[str]:
    r"""Find the columns with a date type.

    Args:
        dtypes: The mapping of column names and data types.

    Returns:
        The columns with a date type.
    """
    columns = []
    for col, dtype in dtypes.items():
        if pa.types.is_date(dtype):
            columns.append(col)
    return columns


def get_dtypes_from_schema(schema: pa.Schema) -> dict[str, pa.DataType]:
    r"""Return the column data types from the schema.

    Args:
        schema: The table schema.

    Returns:
        The mapping of column names and data types.

    Example usage:

    ```pycon
    >>> import pyarrow
    >>> from flamme.utils.dtype import get_dtypes_from_schema
    >>> schema = pyarrow.schema([("number", pyarrow.int32()), ("string", pyarrow.string())])
    >>> dtypes = get_dtypes_from_schema(schema)
    >>> dtypes
    {'number': DataType(int32), 'string': DataType(string)}

    ```
    """
    return dict(zip(schema.names, schema.types))
