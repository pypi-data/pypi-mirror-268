r"""Contain the base class to implement an analyzer."""

from __future__ import annotations

__all__ = ["BaseAnalyzer", "setup_analyzer"]

import logging
from abc import ABC
from typing import TYPE_CHECKING

from objectory import AbstractFactory
from objectory.utils import is_object_config

if TYPE_CHECKING:
    from pandas import DataFrame

    from flamme.section import BaseSection

logger = logging.getLogger(__name__)


class BaseAnalyzer(ABC, metaclass=AbstractFactory):
    r"""Define the base class to analyze a DataFrame.

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
    >>> analyzer.analyze(frame)

    ```
    """

    def analyze(self, frame: DataFrame) -> BaseSection:
        r"""Analyze the data in a DataFrame.

        Args:
            frame: The DataFrame with the data to analyze.

        Returns:
            The section report.

        Example usage:

        ```pycon
        >>> import numpy as np
        >>> import pandas as pd
        >>> from flamme.analyzer import NullValueAnalyzer
        >>> analyzer = NullValueAnalyzer()
        >>> frame = pd.DataFrame(
        ...     {
        ...         "int": np.array([np.nan, 1, 0, 1]),
        ...         "float": np.array([1.2, 4.2, np.nan, 2.2]),
        ...         "str": np.array(["A", "B", None, np.nan]),
        ...     }
        ... )
        >>> analyzer.analyze(frame)

        ```
        """


def is_analyzer_config(config: dict) -> bool:
    r"""Indicate if the input configuration is a configuration for a
    ``BaseAnalyzer``.

    This function only checks if the value of the key  ``_target_``
    is valid. It does not check the other values. If ``_target_``
    indicates a function, the returned type hint is used to check
    the class.

    Args:
        config: The configuration to check.

    Returns:
        ``True`` if the input configuration is a configuration
            for a ``BaseAnalyzer`` object.

    Example usage:

    ```pycon
    >>> from flamme.analyzer import is_analyzer_config
    >>> is_analyzer_config({"_target_": "flamme.analyzer.NullValueAnalyzer"})
    True

    ```
    """
    return is_object_config(config, BaseAnalyzer)


def setup_analyzer(
    analyzer: BaseAnalyzer | dict,
) -> BaseAnalyzer:
    r"""Set up an analyzer.

    The analyzer is instantiated from its configuration
    by using the ``BaseAnalyzer`` factory function.

    Args:
        analyzer: Specifies an analyzer or its configuration.

    Returns:
        An instantiated analyzer.

    Example usage:

    ```pycon
    >>> from flamme.analyzer import setup_analyzer
    >>> analyzer = setup_analyzer({"_target_": "flamme.analyzer.NullValueAnalyzer"})
    >>> analyzer
    NullValueAnalyzer(figsize=None)

    ```
    """
    if isinstance(analyzer, dict):
        logger.info("Initializing an analyzer from its configuration... ")
        analyzer = BaseAnalyzer.factory(**analyzer)
    if not isinstance(analyzer, BaseAnalyzer):
        logger.warning(f"analyzer is not a `BaseAnalyzer` (received: {type(analyzer)})")
    return analyzer
