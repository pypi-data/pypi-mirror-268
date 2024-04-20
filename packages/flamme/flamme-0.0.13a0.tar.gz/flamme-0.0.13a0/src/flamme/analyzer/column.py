r"""Implement an analyzer to analyze only a subset of the columns."""

from __future__ import annotations

__all__ = ["ColumnSubsetAnalyzer"]

import logging
from typing import TYPE_CHECKING

from coola.utils import str_indent, str_mapping

from flamme.analyzer.base import BaseAnalyzer
from flamme.utils import setup_object

if TYPE_CHECKING:
    from collections.abc import Sequence

    from pandas import DataFrame

    from flamme.section import BaseSection

logger = logging.getLogger(__name__)


class ColumnSubsetAnalyzer(BaseAnalyzer):
    r"""Implement an analyzer to analyze only a subset of the columns.

    Args:
        columns: Soecifies the columns to select.
        analyzer: The analyzer
            or its configuration.

    Example usage:

    ```pycon
    >>> import numpy as np
    >>> import pandas as pd
    >>> from flamme.analyzer import ColumnSubsetAnalyzer, NullValueAnalyzer
    >>> analyzer = ColumnSubsetAnalyzer(columns=["int", "float"], analyzer=NullValueAnalyzer())
    >>> analyzer
    ColumnSubsetAnalyzer(
      (columns): 2 ['int', 'float']
      (analyzer): NullValueAnalyzer(figsize=None)
    )
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

    def __init__(self, columns: Sequence[str], analyzer: BaseAnalyzer | dict) -> None:
        self._columns = list(columns)
        self._analyzer = setup_object(analyzer)

    def __repr__(self) -> str:
        args = str_indent(
            str_mapping(
                {"columns": f"{len(self._columns)} {self._columns}", "analyzer": self._analyzer}
            )
        )
        return f"{self.__class__.__qualname__}(\n  {args}\n)"

    def analyze(self, frame: DataFrame) -> BaseSection:
        logger.info(f"Selecting a {len(self._columns):,} columns: {self._columns}")
        frame = frame[self._columns]
        return self._analyzer.analyze(frame)
