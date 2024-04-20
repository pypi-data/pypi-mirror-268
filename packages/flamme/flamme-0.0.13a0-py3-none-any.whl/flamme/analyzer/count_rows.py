r"""Implement an analyzer that generates a section about the number of
rows per temporal window."""

from __future__ import annotations

__all__ = ["TemporalRowCountAnalyzer"]

import logging
from typing import TYPE_CHECKING

from flamme.analyzer.base import BaseAnalyzer
from flamme.section import EmptySection, TemporalRowCountSection

if TYPE_CHECKING:
    from pandas import DataFrame

logger = logging.getLogger(__name__)


class TemporalRowCountAnalyzer(BaseAnalyzer):
    r"""Implement an analyzer to show the number of rows per temporal
    window.

    Args:
        dt_column: The datetime column used to analyze
            the temporal distribution.
        period: The temporal period e.g. monthly or daily.
        figsize: The figure size in inches. The first
            dimension is the width and the second is the height.

    Example usage:

    ```pycon
    >>> import numpy as np
    >>> import pandas as pd
    >>> from flamme.analyzer import TemporalRowCountAnalyzer
    >>> analyzer = TemporalRowCountAnalyzer(dt_column="datetime", period="M")
    >>> analyzer
    TemporalRowCountAnalyzer(dt_column=datetime, period=M, figsize=None)
    >>> frame = pd.DataFrame(
    ...     {
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

    def analyze(self, frame: DataFrame) -> TemporalRowCountSection | EmptySection:
        logger.info(
            f"Analyzing the number of rows | "
            f"datetime column: {self._dt_column} | period: {self._period}"
        )
        if self._dt_column not in frame:
            logger.info(
                "Skipping number of rows analysis because the datetime column "
                f"({self._dt_column}) is not in the DataFrame: {sorted(frame.columns)}"
            )
            return EmptySection()
        return TemporalRowCountSection(
            frame=frame,
            dt_column=self._dt_column,
            period=self._period,
            figsize=self._figsize,
        )
