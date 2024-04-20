r"""Implement an analyzer that generates a summary of the DataFrame."""

from __future__ import annotations

__all__ = ["DataFrameSummaryAnalyzer"]

import logging
from typing import TYPE_CHECKING

from flamme.analyzer.base import BaseAnalyzer
from flamme.section import DataFrameSummarySection

if TYPE_CHECKING:
    from pandas import DataFrame

logger = logging.getLogger(__name__)


class DataFrameSummaryAnalyzer(BaseAnalyzer):
    r"""Implement an analyzer to show a summary of the DataFrame.

    Args:
        top: The number of most frequent values to show.
        sort: If ``True``, sort the columns by alphabetical order.

    Example usage:

    ```pycon
    >>> import numpy as np
    >>> import pandas as pd
    >>> from flamme.analyzer import DataFrameSummaryAnalyzer
    >>> analyzer = DataFrameSummaryAnalyzer()
    >>> analyzer
    DataFrameSummaryAnalyzer(top=5, sort=False)
    >>> frame = pd.DataFrame(
    ...     {
    ...         "col1": np.array([0, 1, 0, 1]),
    ...         "col2": np.array([1, 0, 1, 0]),
    ...         "col3": np.array([1, 1, 1, 1]),
    ...     }
    ... )
    >>> section = analyzer.analyze(frame)

    ```
    """

    def __init__(self, top: int = 5, sort: bool = False) -> None:
        if top < 0:
            msg = f"Incorrect top value ({top}). top must be positive"
            raise ValueError(msg)
        self._top = top
        self._sort = bool(sort)

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}(top={self._top:,}, sort={self._sort})"

    def analyze(self, frame: DataFrame) -> DataFrameSummarySection:
        logger.info("Analyzing the DataFrame...")
        if self._sort:
            frame = frame.reindex(sorted(frame.columns), axis=1)
        return DataFrameSummarySection(frame=frame, top=self._top)
