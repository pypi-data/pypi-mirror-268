r"""Implement an analyzer that generates a section to analyze the data
types of each column."""

from __future__ import annotations

__all__ = ["DataTypeAnalyzer"]

import logging
from typing import TYPE_CHECKING

from flamme.analyzer.base import BaseAnalyzer
from flamme.section import DataTypeSection
from flamme.utils.dtype import frame_column_types

if TYPE_CHECKING:
    from pandas import DataFrame

logger = logging.getLogger(__name__)


class DataTypeAnalyzer(BaseAnalyzer):
    r"""Implement an analyzer to find all the value types in each column.

    Example usage:

    ```pycon
    >>> import numpy as np
    >>> import pandas as pd
    >>> from flamme.analyzer import DataTypeAnalyzer
    >>> analyzer = DataTypeAnalyzer()
    >>> analyzer
    DataTypeAnalyzer()
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

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}()"

    def analyze(self, frame: DataFrame) -> DataTypeSection:
        logger.info("Analyzing the data types...")
        return DataTypeSection(dtypes=frame.dtypes.to_dict(), types=frame_column_types(frame))
