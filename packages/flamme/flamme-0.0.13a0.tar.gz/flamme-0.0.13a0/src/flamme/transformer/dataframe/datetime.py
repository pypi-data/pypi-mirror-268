r"""Contain ``pandas.DataFrame`` transformers to transform columns with
datetime values."""

from __future__ import annotations

__all__ = ["ToDatetimeDataFrameTransformer"]

import logging
from typing import TYPE_CHECKING, Any

import pandas as pd
from tqdm import tqdm

from flamme.transformer.dataframe.base import BaseDataFrameTransformer
from flamme.utils.dtype import find_date_columns_from_dtypes, get_dtypes_from_schema

if TYPE_CHECKING:
    from collections.abc import Sequence

    import pyarrow as pa

logger = logging.getLogger(__name__)


class ToDatetimeDataFrameTransformer(BaseDataFrameTransformer):
    r"""Implement a transformer to convert some columns to numeric type.

    Args:
        columns: The columns to convert.
        **kwargs: The keyword arguments for ``pandas.to_datetime``.

    Example usage:

    ```pycon

    >>> import pandas as pd
    >>> from flamme.transformer.dataframe import ToDatetime
    >>> transformer = ToDatetime(columns=["col1"])
    >>> transformer
    ToDatetimeDataFrameTransformer(columns=('col1',))
    >>> frame = pd.DataFrame(
    ...     {
    ...         "col1": ["2020-1-1", "2020-1-2", "2020-1-31", "2020-12-31", "2021-12-31"],
    ...         "col2": [1, 2, 3, 4, 5],
    ...         "col3": ["a", "b", "c", "d", "e"],
    ...     }
    ... )
    >>> frame.dtypes
    col1    object
    col2     int64
    col3    object
    dtype: object
    >>> out = transformer.transform(frame)
    >>> out.dtypes
    col1    datetime64[ns]
    col2             int64
    col3            object
    dtype: object

    ```
    """

    def __init__(self, columns: Sequence[str], **kwargs: Any) -> None:
        self._columns = tuple(columns)
        self._kwargs = kwargs

    def __repr__(self) -> str:
        args = ", ".join([f"{key}={value}" for key, value in self._kwargs.items()])
        if args:
            args = ", " + args
        return f"{self.__class__.__qualname__}(columns={self._columns}{args})"

    def transform(self, frame: pd.DataFrame) -> pd.DataFrame:
        for col in tqdm(self._columns, desc="Converting to numeric type"):
            frame[col] = pd.to_datetime(frame[col], **self._kwargs)
        return frame

    @classmethod
    def from_schema(cls, schema: pa.Schema, **kwargs: Any) -> ToDatetimeDataFrameTransformer:
        r"""Instantiate a ``ToDatetimeDataFrameTransformer`` where the
        columns are automatically selected from the schema.

        Args:
            schema: The DataFrame schema.
            **kwargs: The keyword arguments for ``pandas.to_datetime``.

        Returns:
            An instantiated ``ToDatetimeDataFrameTransformer``.

        Example usage:

        ```pycon

        >>> import pandas as pd
        >>> import pyarrow as pa
        >>> from flamme.transformer.dataframe import ToDatetime
        >>> transformer = ToDatetime.from_schema(
        ...     pa.schema([("col1", pa.date64()), ("col2", pa.string()), ("col3", pa.int64())])
        ... )
        >>> transformer
        ToDatetimeDataFrameTransformer(columns=('col1',))
        >>> frame = pd.DataFrame(
        ...     {
        ...         "col1": ["2020-1-1", "2020-1-2", "2020-1-31", "2020-12-31", "2021-12-31"],
        ...         "col2": [1, 2, 3, 4, 5],
        ...         "col3": ["a", "b", "c", "d", "e"],
        ...     }
        ... )
        >>> frame.dtypes
        col1    object
        col2     int64
        col3    object
        dtype: object
        >>> out = transformer.transform(frame)
        >>> out.dtypes
        col1    datetime64[ns]
        col2             int64
        col3            object
        dtype: object

        ```
        """
        dtypes = get_dtypes_from_schema(schema)
        columns = sorted(find_date_columns_from_dtypes(dtypes))
        logger.info(f"found {len(columns):,} datetime columns: {columns}")
        return cls(columns=columns, **kwargs)
