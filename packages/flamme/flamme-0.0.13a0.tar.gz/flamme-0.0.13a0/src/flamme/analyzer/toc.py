r"""Implement an analyzer that generates a table of content section."""

from __future__ import annotations

__all__ = ["TableOfContentAnalyzer"]

import logging
from typing import TYPE_CHECKING

from coola.utils import str_indent, str_mapping

from flamme.analyzer.base import BaseAnalyzer, setup_analyzer
from flamme.section.toc import TableOfContentSection

if TYPE_CHECKING:
    from pandas import DataFrame

logger = logging.getLogger(__name__)


class TableOfContentAnalyzer(BaseAnalyzer):
    r"""Implement a wrapper around an analyzer to add a table of content
    to the generated section report.

    Args:
        analyzer: The analyzer or its configuration.
        max_toc_depth: The maximum level to show in the
            table of content.

    Example usage:

    ```pycon
    >>> import numpy as np
    >>> import pandas as pd
    >>> from flamme.analyzer import TableOfContentAnalyzer, DuplicatedRowAnalyzer
    >>> analyzer = TableOfContentAnalyzer(DuplicatedRowAnalyzer())
    >>> analyzer
    TableOfContentAnalyzer(
      (analyzer): DuplicatedRowAnalyzer(columns=None, figsize=None)
      (max_toc_depth): 1
    )
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

    def __init__(
        self,
        analyzer: BaseAnalyzer | dict,
        max_toc_depth: int = 1,
    ) -> None:
        self._analyzer = setup_analyzer(analyzer)
        self._max_toc_depth = max_toc_depth

    def __repr__(self) -> str:
        args = str_indent(
            str_mapping({"analyzer": self._analyzer, "max_toc_depth": self._max_toc_depth})
        )
        return f"{self.__class__.__qualname__}(\n  {args}\n)"

    def analyze(self, frame: DataFrame) -> TableOfContentSection:
        return TableOfContentSection(
            section=self._analyzer.analyze(frame), max_toc_depth=self._max_toc_depth
        )
