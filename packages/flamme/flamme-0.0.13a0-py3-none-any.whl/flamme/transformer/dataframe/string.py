r"""Contain ``pandas.DataFrame`` transformers to transform columns with
string values."""

from __future__ import annotations

__all__ = ["StripStringDataFrameTransformer"]

from typing import TYPE_CHECKING

from tqdm import tqdm

from flamme.transformer.dataframe.base import BaseDataFrameTransformer

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pandas import DataFrame


class StripStringDataFrameTransformer(BaseDataFrameTransformer):
    r"""Implement a transformer to strip the strings of some columns.

    Args:
        columns: The columns to process.

    Example usage:

    ```pycon
    >>> import pandas as pd
    >>> from flamme.transformer.dataframe import StripString
    >>> transformer = StripString(columns=["col1", "col3"])
    >>> transformer
    StripStringDataFrameTransformer(columns=('col1', 'col3'))
    >>> frame = pd.DataFrame(
    ...     {
    ...         "col1": [1, 2, 3, 4, 5],
    ...         "col2": ["1", "2", "3", "4", "5"],
    ...         "col3": ["a ", " b", "  c  ", "d", "e"],
    ...         "col4": ["a ", " b", "  c  ", "d", "e"],
    ...     }
    ... )
    >>> frame
       col1 col2   col3   col4
    0     1    1     a      a
    1     2    2      b      b
    2     3    3    c      c
    3     4    4      d      d
    4     5    5      e      e
    >>> out = transformer.transform(frame)
    >>> out
       col1 col2 col3   col4
    0     1    1    a     a
    1     2    2    b      b
    2     3    3    c    c
    3     4    4    d      d
    4     5    5    e      e

    ```
    """

    def __init__(self, columns: Sequence[str]) -> None:
        self._columns = tuple(columns)

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}(columns={self._columns})"

    def transform(self, frame: DataFrame) -> DataFrame:
        for col in tqdm(self._columns, desc="Striping strings"):
            frame[col] = frame[col].apply(lambda x: x.strip() if isinstance(x, str) else x)
        return frame
