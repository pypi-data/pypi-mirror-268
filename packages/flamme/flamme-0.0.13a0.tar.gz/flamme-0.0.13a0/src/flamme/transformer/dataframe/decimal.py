r"""Contain ``pandas.DataFrame`` transformers to transform columns with
decimal values."""

from __future__ import annotations

__all__ = ["DecimalToNumericDataFrameTransformer"]

from typing import TYPE_CHECKING, Any

import pandas as pd
from tqdm import tqdm

from flamme.transformer.dataframe.base import BaseDataFrameTransformer
from flamme.utils.filtering import find_columns_decimal

if TYPE_CHECKING:
    from pandas import DataFrame


class DecimalToNumericDataFrameTransformer(BaseDataFrameTransformer):
    r"""Implement a ``pandas.DataFrame`` to convert all the columns with
    ``Decimal`` objects to floats.

    Args:
        **kwargs: The keyword arguments for
            ``pandas.to_numeric``.

    Example usage:

    .. code-block:: pycon

        >>> from decimal import Decimal
        >>> import pandas as pd
        >>> from flamme.transformer.dataframe import DecimalToNumeric
        >>> transformer = DecimalToNumericDataFrameTransformer()
        >>> transformer
        DecimalToNumericDataFrameTransformer()
        >>> frame = pd.DataFrame(
        ...     {
        ...         "col1": [1, 2, 3, 4, Decimal(5)],
        ...         "col2": [Decimal(1), Decimal(2), Decimal(3), Decimal(4), Decimal(5)],
        ...         "col3": ["1", "2", "3", "4", "5"],
        ...         "col4": ["a", "b", "c", "d", "e"],
        ...     }
        ... )
        >>> frame.dtypes
        col1    object
        col2    object
        col3    object
        col4    object
        dtype: object
        >>> out = transformer.transform(frame)
        >>> out.dtypes
        col1     int64
        col2   float64
        col3    object
        col4    object
        dtype: object
    """

    def __init__(self, **kwargs: Any) -> None:
        self._kwargs = kwargs

    def __repr__(self) -> str:
        args = ", ".join([f"{key}={value}" for key, value in self._kwargs.items()])
        return f"{self.__class__.__qualname__}({args})"

    def transform(self, frame: DataFrame) -> DataFrame:
        columns = find_columns_decimal(frame)
        for col in tqdm(columns, desc="Converting Decimal to numeric type"):
            frame[col] = pd.to_numeric(frame[col], **self._kwargs)
        return frame
