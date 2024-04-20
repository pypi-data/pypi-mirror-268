r"""Implement an analyzer that generates a section to analyze the
temporal distribution of null values for all columns."""

from __future__ import annotations

__all__ = ["GlobalTemporalNullValueAnalyzer"]

import logging
from typing import TYPE_CHECKING

from flamme.analyzer.base import BaseAnalyzer
from flamme.section import EmptySection, GlobalTemporalNullValueSection

if TYPE_CHECKING:
    from pandas import DataFrame

logger = logging.getLogger(__name__)


class GlobalTemporalNullValueAnalyzer(BaseAnalyzer):
    r"""Implement an analyzer to show the temporal distribution of null
    values for all columns.

    Args:
        dt_column: The datetime column used to analyze
            the temporal distribution.
        period: The temporal period e.g. monthly or
            daily.
        figsize: The figure size in inches. The first
            dimension is the width and the second is the height.

    Example usage:

    ```pycon
    >>> import numpy as np
    >>> import pandas as pd
    >>> from flamme.analyzer import GlobalTemporalNullValueAnalyzer
    >>> analyzer = GlobalTemporalNullValueAnalyzer(dt_column="datetime", period="M")
    >>> analyzer
    GlobalTemporalNullValueAnalyzer(dt_column=datetime, period=M, figsize=None)
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
        dt_column: str,
        period: str,
        figsize: tuple[float, float] | None = None,
    ) -> None:
        self._dt_column = dt_column
        self._period = period
        self._figsize = figsize

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__qualname__}(dt_column={self._dt_column}, "
            f"period={self._period}, figsize={self._figsize})"
        )

    def analyze(self, frame: DataFrame) -> GlobalTemporalNullValueSection | EmptySection:
        logger.info(
            f"Analyzing the temporal null value distribution | "
            f"datetime column: {self._dt_column} | period: {self._period}"
        )
        if self._dt_column not in frame:
            logger.info(
                "Skipping temporal null value analysis because the datetime column "
                f"({self._dt_column}) is not in the DataFrame: {sorted(frame.columns)}"
            )
            return EmptySection()
        return GlobalTemporalNullValueSection(
            frame=frame,
            dt_column=self._dt_column,
            period=self._period,
            figsize=self._figsize,
        )
