r"""Contain ``pandas.Series`` transformers to transform datetime
columns."""

from __future__ import annotations

__all__ = ["ToDatetimeSeriesTransformer"]

from typing import Any

import pandas as pd

from flamme.transformer.series.base import BaseSeriesTransformer


class ToDatetimeSeriesTransformer(BaseSeriesTransformer):
    r"""Implement a transformer to convert a ``pandas.Series`` to
    datetime type.

    Args:
        **kwargs: The keyword arguments for
            ``pandas.to_datetime``.

    Example usage:

    ```pycon
    >>> import pandas as pd
    >>> from flamme.transformer.series import ToDatetime
    >>> transformer = ToDatetime()
    >>> transformer
    ToDatetimeSeriesTransformer()
    >>> series = pd.Series(["2020-1-1", "2020-1-2", "2020-1-31", "2020-12-31", "2021-12-31"])
    >>> series.dtype
    dtype('O')
    >>> out = transformer.transform(series)
    >>> out.dtype
    dtype('<M8[ns]')

    ```
    """

    def __init__(self, **kwargs: Any) -> None:
        self._kwargs = kwargs

    def __repr__(self) -> str:
        args = ", ".join([f"{key}={value}" for key, value in self._kwargs.items()])
        return f"{self.__class__.__qualname__}({args})"

    def transform(self, series: pd.Series) -> pd.Series:
        return pd.to_datetime(series, **self._kwargs)
