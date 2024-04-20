r"""Contain ``pandas.DataFrame`` transformers to select columns in
DataFrames."""

from __future__ import annotations

__all__ = ["ColumnSelectionDataFrameTransformer"]

import logging
from typing import TYPE_CHECKING

from flamme.transformer.dataframe.base import BaseDataFrameTransformer

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pandas import DataFrame

logger = logging.getLogger(__name__)


class ColumnSelectionDataFrameTransformer(BaseDataFrameTransformer):
    r"""Implement a ``pandas.DataFrame`` transformer to select a subset
    of columns.

    Args:
        columns: The columns to keep.
        ignore_missing: If ``False``, an exception is raised if a
            column is missing, otherwise a warning message is shown.

    Example usage:

    ```pycon
    >>> import pandas as pd
    >>> from flamme.transformer.dataframe import ColumnSelection
    >>> transformer = ColumnSelection(columns=["col1", "col2"])
    >>> transformer
    ColumnSelectionDataFrameTransformer(columns=['col1', 'col2'], ignore_missing=False)
    >>> frame = pd.DataFrame(
    ...     {
    ...         "col1": ["2020-1-1", "2020-1-2", "2020-1-31", "2020-12-31", None],
    ...         "col2": [1, 2, 3, 4, 5],
    ...         "col3": ["a", "b", "c", "d", "e"],
    ...     }
    ... )
    >>> out = transformer.transform(frame)
    >>> out
             col1  col2
    0    2020-1-1     1
    1    2020-1-2     2
    2   2020-1-31     3
    3  2020-12-31     4
    4        None     5

    ```
    """

    def __init__(self, columns: Sequence[str], ignore_missing: bool = False) -> None:
        self._columns = list(columns)
        self._ignore_missing = bool(ignore_missing)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__qualname__}(columns={self._columns}, "
            f"ignore_missing={self._ignore_missing})"
        )

    def transform(self, frame: DataFrame) -> DataFrame:
        columns = []
        for col in self._columns:
            if col not in frame:
                if self._ignore_missing:
                    logger.warning(f"Column `{col}` is not in the DataFrame")
                else:
                    msg = (
                        f"Column `{col}` is not in the DataFrame (columns:{sorted(frame.columns)})"
                    )
                    raise RuntimeError(msg)
            else:
                columns.append(col)
        logger.info(f"Selecting {len(columns):,} columns: {columns}")
        out = frame[columns].copy()
        logger.info(f"DataFrame shape after the column selection: {out.shape}")
        return out
