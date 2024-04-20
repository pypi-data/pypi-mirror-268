r"""Contain ``pandas.Series`` transformers to transform columns with
string values."""

from __future__ import annotations

__all__ = ["StripStringSeriesTransformer"]

from typing import TYPE_CHECKING

from flamme.transformer.series.base import BaseSeriesTransformer

if TYPE_CHECKING:
    from pandas import Series


class StripStringSeriesTransformer(BaseSeriesTransformer):
    r"""Implement a transformer to strip the strings in a
    ``pandas.Series``.

    Example usage:

    ```pycon
    >>> import pandas as pd
    >>> from flamme.transformer.series import StripString
    >>> transformer = StripString()
    >>> transformer
    StripStringSeriesTransformer()
    >>> series = pd.Series(["a ", " b", "  c  ", " d ", "e"])
    >>> out = transformer.transform(series)
    >>> out
    0    a
    1    b
    2    c
    3    d
    4    e
    dtype: object

    ```
    """

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}()"

    def transform(self, series: Series) -> Series:
        return series.apply(lambda x: x.strip() if isinstance(x, str) else x)
