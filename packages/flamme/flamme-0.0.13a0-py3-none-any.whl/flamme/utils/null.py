r"""Contain utility functions to analyze data with null values."""

from __future__ import annotations

__all__ = ["compute_null_per_col"]

import numpy as np
from pandas import DataFrame


def compute_null_per_col(frame: DataFrame) -> DataFrame:
    r"""Return the number and percentage of null values per column.

    Args:
        frame: The DataFrame to analyze.

    Returns:
        A DataFrame with the number and percentage of null values per
            column.

    Example usage:

    ```pycon
    >>> import pandas as pd
    >>> from flamme.utils.null import compute_null_per_col
    >>> frame = compute_null_per_col(
    ...     pd.DataFrame(
    ...         {
    ...             "int": np.array([np.nan, 1, 0, 1]),
    ...             "float": np.array([1.2, 4.2, np.nan, 2.2]),
    ...             "str": np.array(["A", "B", None, np.nan]),
    ...         }
    ...     )
    ... )
    >>> frame
      column  null  total  null_pct
    0    int     1      4      0.25
    1  float     1      4      0.25
    2    str     2      4      0.50

    ```
    """
    null_count = frame.isna().sum().to_frame("count")["count"].to_numpy().astype(int)
    total_count = np.full((frame.shape[1],), frame.shape[0]).astype(int)
    with np.errstate(invalid="ignore"):
        null_pct = null_count.astype(float) / total_count.astype(float)
    return DataFrame(
        {
            "column": list(frame.columns),
            "null": null_count,
            "total": total_count,
            "null_pct": null_pct,
        }
    )
