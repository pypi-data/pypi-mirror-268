r"""Contain ``pandas.DataFrame`` transformers to transform columns with
null values."""

from __future__ import annotations

__all__ = ["NullColumnDataFrameTransformer"]

import logging
from typing import TYPE_CHECKING

from flamme.transformer.dataframe.base import BaseDataFrameTransformer
from flamme.utils.null import compute_null_per_col

if TYPE_CHECKING:
    from pandas import DataFrame

logger = logging.getLogger(__name__)


class NullColumnDataFrameTransformer(BaseDataFrameTransformer):
    r"""Implement a ``pandas.DataFrame`` transformer to remove the
    columns that have too many null values.

    Args:
        threshold (float): The maximum percentage of null
            values to keep columns. If the proportion of null vallues
            is greater or equal to this threshold value, the column
            is removed. If set to ``1.0``, it removes all the columns
            that have only null values.

    Example usage:

    .. code-block:: pycon

        >>> import pandas as pd
        >>> from flamme.transformer.dataframe import NullColumn
        >>> transformer = NullColumn(threshold=1.0)
        >>> transformer
        NullColumnDataFrameTransformer(threshold=1.0)
        >>> frame = pd.DataFrame(
        ...     {
        ...         "col1": ["2020-1-1", "2020-1-2", "2020-1-31", "2020-12-31", None],
        ...         "col2": [1, None, 3, None, 5],
        ...         "col3": [None, None, None, None, None],
        ...     }
        ... )
        >>> out = transformer.transform(frame)
        >>> out
                 col1  col2
        0    2020-1-1   1.0
        1    2020-1-2   NaN
        2   2020-1-31   3.0
        3  2020-12-31   NaN
        4        None   5.0
    """

    def __init__(self, threshold: float) -> None:
        self._threshold = float(threshold)

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}(threshold={self._threshold})"

    def transform(self, frame: DataFrame) -> DataFrame:
        if frame.shape[0] == 0:
            return frame
        num_orig_cols = len(frame.columns)
        frame_null = compute_null_per_col(frame)
        columns = frame_null[frame_null["null_pct"] < self._threshold]["column"].tolist()
        logger.info(
            f"Removing {num_orig_cols - len(columns):,} columns because they have too "
            f"many null values (threshold={self._threshold})..."
        )
        return frame[columns].copy()
