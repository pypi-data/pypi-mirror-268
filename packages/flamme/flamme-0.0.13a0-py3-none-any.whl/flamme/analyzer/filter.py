r"""Implement an analyzer that filters the data before to analyze the
data."""

from __future__ import annotations

__all__ = ["FilteredAnalyzer"]

import logging
from typing import TYPE_CHECKING

from coola.utils import str_indent, str_mapping

from flamme.analyzer.base import BaseAnalyzer, setup_analyzer

if TYPE_CHECKING:
    from pandas import DataFrame

    from flamme.section import BaseSection

logger = logging.getLogger(__name__)


class FilteredAnalyzer(BaseAnalyzer):
    r"""Implement an analyzer that filters the data before to analyze the
    data.

    Args:
        query: Soecifies the query.
        analyzer: The analyzer or its configuration.

    Example usage:

    ```pycon
    >>> import numpy as np
    >>> import pandas as pd
    >>> from flamme.analyzer import FilteredAnalyzer, NullValueAnalyzer
    >>> analyzer = FilteredAnalyzer(query="float >= 2.0", analyzer=NullValueAnalyzer())
    >>> analyzer
    FilteredAnalyzer(
      (query): float >= 2.0
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

    def __init__(self, query: str, analyzer: BaseAnalyzer | dict) -> None:
        self._query = query
        self._analyzer = setup_analyzer(analyzer)

    def __repr__(self) -> str:
        args = str_indent(str_mapping({"query": self._query, "analyzer": self._analyzer}))
        return f"{self.__class__.__qualname__}(\n  {args}\n)"

    def analyze(self, frame: DataFrame) -> BaseSection:
        logger.info("Filtering the DataFrame...")
        frame = frame.query(self._query)
        return self._analyzer.analyze(frame)
