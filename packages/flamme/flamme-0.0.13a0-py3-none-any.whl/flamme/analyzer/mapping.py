r"""Implement analyzer that combine multiple analyzers."""

from __future__ import annotations

__all__ = ["MappingAnalyzer"]

from typing import TYPE_CHECKING

from coola.utils import str_indent, str_mapping

from flamme.analyzer.base import BaseAnalyzer, setup_analyzer
from flamme.section import SectionDict

if TYPE_CHECKING:
    from collections.abc import Mapping

    from pandas import DataFrame


class MappingAnalyzer(BaseAnalyzer):
    r"""Implement an analyzer that combine multiple analyzers.

    Args:
        analyzers: The mappings to analyze.
            The key of each analyzer is used to organize the metrics
            and report.
        max_toc_depth: The maximum level to show in the
            table of content. Set this value to ``0`` to not show
            the table of content at the beginning of the section.

    Example usage:

    ```pycon
    >>> import numpy as np
    >>> import pandas as pd
    >>> from flamme.analyzer import (
    ...     FilteredAnalyzer,
    ...     NullValueAnalyzer,
    ...     DuplicatedRowAnalyzer,
    ...     MappingAnalyzer,
    ... )
    >>> analyzer = MappingAnalyzer(
    ...     {"null": NullValueAnalyzer(), "duplicate": DuplicatedRowAnalyzer()}
    ... )
    >>> analyzer
    MappingAnalyzer(
      (null): NullValueAnalyzer(figsize=None)
      (duplicate): DuplicatedRowAnalyzer(columns=None, figsize=None)
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

    def __init__(
        self, analyzers: Mapping[str, BaseAnalyzer | dict], max_toc_depth: int = 0
    ) -> None:
        self._analyzers = {name: setup_analyzer(analyzer) for name, analyzer in analyzers.items()}
        self._max_toc_depth = max_toc_depth

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}(\n  {str_indent(str_mapping(self._analyzers))}\n)"

    @property
    def analyzers(self) -> dict[str, BaseAnalyzer]:
        return self._analyzers

    def analyze(self, frame: DataFrame) -> SectionDict:
        return SectionDict(
            sections={name: analyzer.analyze(frame) for name, analyzer in self._analyzers.items()},
            max_toc_depth=self._max_toc_depth,
        )

    def add_analyzer(self, key: str, analyzer: BaseAnalyzer, replace_ok: bool = False) -> None:
        r"""Add an analyzer to the current analyzer.

        Args:
            key: The key of the analyzer.
            analyzer: The analyzer to add.
            replace_ok: If ``False``, ``KeyError`` is raised if an
                analyzer with the same key exists. If ``True``,
                the new analyzer will replace the existing analyzer.

        Raises:
            KeyError: if an  analyzer with the same key exists.

        Example usage:

        ```pycon
        >>> import numpy as np
        >>> import pandas as pd
        >>> from flamme.analyzer import MappingAnalyzer, NullValueAnalyzer, DuplicatedRowAnalyzer
        >>> analyzer = MappingAnalyzer({"null": NullValueAnalyzer()})
        >>> analyzer.add_analyzer("duplicate", DuplicatedRowAnalyzer())
        >>> analyzer
        MappingAnalyzer(
          (null): NullValueAnalyzer(figsize=None)
          (duplicate): DuplicatedRowAnalyzer(columns=None, figsize=None)
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
        if key in self._analyzers and not replace_ok:
            msg = (
                f"`{key}` is already used to register an analyzer. "
                "Use `replace_ok=True` to replace the analyzer"
            )
            raise KeyError(msg)
        self._analyzers[key] = analyzer
