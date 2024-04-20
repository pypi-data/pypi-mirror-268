r"""Contain ``pandas.Series`` transformers to transform numeric
columns."""

from __future__ import annotations

__all__ = ["ToNumericSeriesTransformer"]

from typing import Any

import pandas as pd

from flamme.transformer.series.base import BaseSeriesTransformer


class ToNumericSeriesTransformer(BaseSeriesTransformer):
    r"""Implement a ``pandas.Series`` transformer to convert a
    ``pandas.Series`` to numeric type.

    Args:
        **kwargs: The keyword arguments for
            ``pandas.to_numeric``.

    Example usage:

    ```pycon
    >>> import pandas as pd
    >>> from flamme.transformer.series import ToNumeric
    >>> transformer = ToNumeric()
    >>> transformer
    ToNumericSeriesTransformer()
    >>> series = pd.Series(["1", "2", "3", "4", "5"])
    >>> series.dtype
    dtype('O')
    >>> out = transformer.transform(series)
    >>> out.dtype
    dtype('int64')

    ```
    """

    def __init__(self, **kwargs: Any) -> None:
        self._kwargs = kwargs

    def __repr__(self) -> str:
        args = ", ".join([f"{key}={value}" for key, value in self._kwargs.items()])
        return f"{self.__class__.__qualname__}({args})"

    def transform(self, series: pd.Series) -> pd.Series:
        return pd.to_numeric(series, **self._kwargs)
