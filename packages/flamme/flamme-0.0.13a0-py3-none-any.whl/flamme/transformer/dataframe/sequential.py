r"""Contain a ``pandas.DataFrame`` transformer to combine sequentially
multiple transformers."""

from __future__ import annotations

__all__ = ["SequentialDataFrameTransformer"]

from typing import TYPE_CHECKING

from coola.utils import str_indent, str_sequence

from flamme.transformer.dataframe.base import (
    BaseDataFrameTransformer,
    setup_dataframe_transformer,
)

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pandas import DataFrame


class SequentialDataFrameTransformer(BaseDataFrameTransformer):
    r"""Implement a ``pandas.DataFrame`` transformer to apply
    sequentially several transformers.

    Args:
        transformers: The transformers or their
            configurations.

    Example usage:

    ```pycon
    >>> import pandas as pd
    >>> from flamme.transformer.dataframe import (
    ...     Sequential,
    ...     StripString,
    ...     ToNumeric,
    ... )
    >>> transformer = Sequential(
    ...     [
    ...         StripString(columns=["col1", "col3"]),
    ...         ToNumeric(columns=["col1", "col2"]),
    ...     ]
    ... )
    >>> transformer
    SequentialDataFrameTransformer(
      (0): StripStringDataFrameTransformer(columns=('col1', 'col3'))
      (1): ToNumericDataFrameTransformer(columns=('col1', 'col2'))
    )
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

    def __init__(self, transformers: Sequence[BaseDataFrameTransformer | dict]) -> None:
        self._transformers = tuple(
            setup_dataframe_transformer(transformer) for transformer in transformers
        )

    def __repr__(self) -> str:
        args = ""
        if self._transformers:
            args = f"\n  {str_indent(str_sequence(self._transformers))}\n"
        return f"{self.__class__.__qualname__}({args})"

    def transform(self, frame: DataFrame) -> DataFrame:
        for transformer in self._transformers:
            frame = transformer.transform(frame)
        return frame
