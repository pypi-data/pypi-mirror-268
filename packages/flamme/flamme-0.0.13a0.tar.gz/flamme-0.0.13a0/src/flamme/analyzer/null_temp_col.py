r"""Implement an analyzer that generates a section to analyze the
temporal distribution of null values for a given column."""

from __future__ import annotations

__all__ = ["ColumnTemporalNullValueAnalyzer"]

import logging
from typing import TYPE_CHECKING

from flamme.analyzer.base import BaseAnalyzer
from flamme.section import ColumnTemporalNullValueSection, EmptySection

if TYPE_CHECKING:
    from pandas import DataFrame

logger = logging.getLogger(__name__)


class ColumnTemporalNullValueAnalyzer(BaseAnalyzer):
    r"""Implement an analyzer to show the temporal distribution of null
    values for a given column.

    Args:
        column: The column to analyze.
        dt_column: The datetime column used to analyze
            the temporal distribution.
        period: The temporal period e.g. monthly or daily.
        figsize: The figure size in inches. The first
            dimension is the width and the second is the height.

    Example usage:

    ```pycon
    >>> import numpy as np
    >>> import pandas as pd
    >>> from flamme.analyzer import TemporalNullValueAnalyzer
    >>> analyzer = ColumnTemporalNullValueAnalyzer(
    ...     column="col", dt_column="datetime", period="M"
    ... )
    >>> analyzer
    ColumnTemporalNullValueAnalyzer(column=col, dt_column=datetime, period=M, figsize=None)
    >>> frame = pd.DataFrame(
    ...     {
    ...         "col": np.array([np.nan, 1, 0, 1]),
    ...         "datetime": pd.to_datetime(
    ...             ["2020-01-03", "2020-02-03", "2020-03-03", "2020-04-03"]
    ...         ),
    ...     }
    ... )
    >>> section = analyzer.analyze(frame)

    ```
    """

    def __init__(
        self,
        column: str,
        dt_column: str,
        period: str,
        figsize: tuple[float, float] | None = None,
    ) -> None:
        self._column = column
        self._dt_column = dt_column
        self._period = period
        self._figsize = figsize

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__qualname__}(column={self._column}, "
            f"dt_column={self._dt_column}, period={self._period}, figsize={self._figsize})"
        )

    def analyze(self, frame: DataFrame) -> ColumnTemporalNullValueSection | EmptySection:
        logger.info(
            f"Analyzing the temporal null value distribution of {self._column} | "
            f"datetime column: {self._dt_column} | period: {self._period}"
        )
        if self._column not in frame:
            logger.info(
                "Skipping temporal null value analysis because the column "
                f"({self._column}) is not in the DataFrame: {sorted(frame.columns)}"
            )
            return EmptySection()
        if self._dt_column not in frame:
            logger.info(
                "Skipping temporal null value analysis because the datetime column "
                f"({self._dt_column}) is not in the DataFrame: {sorted(frame.columns)}"
            )
            return EmptySection()
        return ColumnTemporalNullValueSection(
            frame=frame,
            column=self._column,
            dt_column=self._dt_column,
            period=self._period,
            figsize=self._figsize,
        )
