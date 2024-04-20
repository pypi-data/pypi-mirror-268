r"""Contain utility functions to filter columns in DataFrames."""

from __future__ import annotations

__all__ = [
    "find_columns_decimal",
    "find_columns_str",
    "find_columns_type",
]

from decimal import Decimal
from typing import TYPE_CHECKING

from flamme.utils.dtype import frame_column_types

if TYPE_CHECKING:
    from pandas import DataFrame


def find_columns_type(frame: DataFrame, cls: type) -> tuple[str, ...]:
    r"""Find the list of columns that contains a given type.

    Args:
        frame: The DataFrame to filter.
        cls: The type to find.

    Returns:
        tuple: The tuple of columns with the given type.

    Example usage:

    ```pycon
    >>> import pandas as pd
    >>> from flamme.utils.filtering import find_columns_type
    >>> frame = pd.DataFrame(
    ...     {
    ...         "col1": [1, 2, 3, 4, 5],
    ...         "col2": ["1", "2", "3", "4", "5"],
    ...         "col3": ["1", "2", "3", "4", "5"],
    ...         "col4": ["a", "b", "c", "d", "e"],
    ...     }
    ... )
    >>> find_columns_type(frame, str)
    ('col2', 'col3', 'col4')

    ```
    """
    types = frame_column_types(frame)
    return tuple(col for col, tps in types.items() if cls in tps)


def find_columns_decimal(frame: DataFrame) -> tuple[str, ...]:
    r"""Find the list of columns that contains the type string.

    Args:
        frame: The DataFrame.

    Returns:
        The tuple of columns with the type string.

    Example usage:

    ```pycon
    >>> import pandas as pd
    >>> from decimal import Decimal
    >>> from flamme.utils.filtering import find_columns_decimal
    >>> frame = pd.DataFrame(
    ...     {
    ...         "col1": [1, 2, 3, 4, Decimal(5)],
    ...         "col2": ["1", "2", "3", "4", "5"],
    ...         "col3": ["1", "2", "3", "4", "5"],
    ...         "col4": ["a", "b", "c", "d", "e"],
    ...     }
    ... )
    >>> find_columns_decimal(frame)
    ('col1',)

    ```
    """
    return find_columns_type(frame, Decimal)


def find_columns_str(frame: DataFrame) -> tuple[str, ...]:
    r"""Find the list of columns that contains the type string.

    Args:
        frame: The input DataFrame.

    Returns:
        The tuple of columns with the type string.

    Example usage:

    ```pycon
    >>> import numpy as np
    >>> import pandas as pd
    >>> from flamme.utils.filtering import find_columns_str
    >>> frame = pd.DataFrame(
    ...     {
    ...         "col1": [1, 2, 3, 4, 5],
    ...         "col2": ["1", "2", "3", "4", "5"],
    ...         "col3": ["1", "2", "3", "4", "5"],
    ...         "col4": ["a", "b", "c", "d", "e"],
    ...     }
    ... )
    >>> find_columns_str(frame)
    ('col2', 'col3', 'col4')

    ```
    """
    return find_columns_type(frame, str)
