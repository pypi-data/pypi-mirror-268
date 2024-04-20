r"""Implement an analyzer that generates a section to analyze the number
of null values."""

from __future__ import annotations

__all__ = ["TemporalNullValueAnalyzer", "NullValueAnalyzer"]

import logging
from typing import TYPE_CHECKING

import numpy as np

from flamme.analyzer.base import BaseAnalyzer
from flamme.section import EmptySection
from flamme.section.null import NullValueSection, TemporalNullValueSection

if TYPE_CHECKING:
    from pandas import DataFrame

logger = logging.getLogger(__name__)


class NullValueAnalyzer(BaseAnalyzer):
    r"""Implement a null value analyzer.

    Args:
        figsize: The figure size in inches. The first
            dimension is the width and the second is the height.

    Example usage:

    ```pycon
    >>> import numpy as np
    >>> import pandas as pd
    >>> from flamme.analyzer import NullValueAnalyzer
    >>> analyzer = NullValueAnalyzer()
    >>> analyzer
    NullValueAnalyzer(figsize=None)
    >>> frame = pd.DataFrame(
    ...     {
    ...         "int": np.array([np.nan, 1, 0, 1]),
    ...         "float": np.array([1.2, 4.2, np.nan, 2.2]),
    ...         "str": np.array(["A", "B", None, np.nan]),
    ...     }
    ... )
    >>> section = analyzer.analyze(frame)

    ```
    """

    def __init__(self, figsize: tuple[float, float] | None = None) -> None:
        self._figsize = figsize

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}(figsize={self._figsize})"

    def analyze(self, frame: DataFrame) -> NullValueSection:
        logger.info("Analyzing the null value distribution of all columns...")
        return NullValueSection(
            columns=list(frame.columns),
            null_count=frame.isna().sum().to_frame("count")["count"].to_numpy(),
            total_count=np.full((frame.shape[1],), frame.shape[0]),
            figsize=self._figsize,
        )


class TemporalNullValueAnalyzer(BaseAnalyzer):
    r"""Implement an analyzer to show the temporal distribution of null
    values.

    Args:
        dt_column: The datetime column used to analyze
            the temporal distribution.
        period: The temporal period e.g. monthly or daily.
        ncols: The number of columns.
        figsize: The figure size in inches. The first
            dimension is the width and the second is the height.

    Example usage:

    ```pycon
    >>> import numpy as np
    >>> import pandas as pd
    >>> from flamme.analyzer import TemporalNullValueAnalyzer
    >>> analyzer = TemporalNullValueAnalyzer("datetime", period="M")
    >>> analyzer
    TemporalNullValueAnalyzer(dt_column=datetime, period=M, ncols=2, figsize=(7, 5))
    >>> frame = pd.DataFrame(
    ...     {
    ...         "int": np.array([np.nan, 1, 0, 1]),
    ...         "float": np.array([1.2, 4.2, np.nan, 2.2]),
    ...         "str": np.array(["A", "B", None, np.nan]),
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
        ncols: int = 2,
        figsize: tuple[float, float] = (7, 5),
    ) -> None:
        self._dt_column = dt_column
        self._period = period
        self._ncols = ncols
        self._figsize = figsize

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__qualname__}(dt_column={self._dt_column}, period={self._period}, "
            f"ncols={self._ncols}, figsize={self._figsize})"
        )

    def analyze(self, frame: DataFrame) -> TemporalNullValueSection | EmptySection:
        logger.info(
            "Analyzing the temporal null value distribution of all columns | "
            f"datetime column: {self._dt_column} | period: {self._period}"
        )
        if self._dt_column not in frame:
            logger.info(
                "Skipping monthly null value analysis because the datetime column "
                f"({self._dt_column}) is not in the DataFrame: {sorted(frame.columns)}"
            )
            return EmptySection()
        return TemporalNullValueSection(
            frame=frame,
            dt_column=self._dt_column,
            period=self._period,
            ncols=self._ncols,
            figsize=self._figsize,
        )
