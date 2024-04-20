r"""Contain the base class to implement a ``pandas.Series``
transformer."""

from __future__ import annotations

__all__ = ["BaseSeriesTransformer", "is_series_transformer_config", "setup_series_transformer"]

import logging
from abc import ABC
from typing import TYPE_CHECKING

from objectory import AbstractFactory
from objectory.utils import is_object_config

if TYPE_CHECKING:
    from pandas import Series

logger = logging.getLogger(__name__)


class BaseSeriesTransformer(ABC, metaclass=AbstractFactory):
    r"""Define the base class to transform a ``pandas.Series``.

    Example usage:

    ```pycon
    >>> import pandas as pd
    >>> from flamme.transformer.series import ToNumeric
    >>> transformer = ToNumeric()
    >>> transformer
    ToNumericSeriesTransformer()
    >>> series = pd.Series(["1", "2", "3", "4", "5"])
    >>> series.dtype
    dtype('O')
    >>> out = transformer.transform(series)
    >>> out.dtype
    dtype('int64')

    ```
    """

    def transform(self, series: Series) -> Series:
        r"""Transform a ``pandas.Series``.

        Args:
            series: The ``pandas.Series`` to transform.

        Returns:
            The transformed ``pandas.Series``.

        Example usage:

        ```pycon
        >>> import pandas as pd
        >>> from flamme.transformer.series import ToNumeric
        >>> transformer = ToNumeric()
        >>> series = pd.Series(["1", "2", "3", "4", "5"])
        >>> out = transformer.transform(series)
        >>> out.dtype
        dtype('int64')

        ```
        """


def is_series_transformer_config(config: dict) -> bool:
    r"""Indicate if the input configuration is a configuration for a
    ``BaseSeriesTransformer``.

    This function only checks if the value of the key  ``_target_``
    is valid. It does not check the other values. If ``_target_``
    indicates a function, the returned type hint is used to check
    the class.

    Args:
        config: The configuration to check.

    Returns:
        ``True`` if the input configuration is a configuration
            for a ``BaseSeriesTransformer`` object.

    Example usage:

    ```pycon
    >>> from flamme.transformer.series import is_series_transformer_config
    >>> is_series_transformer_config({"_target_": "flamme.transformer.series.ToNumeric"})
    True

    ```
    """
    return is_object_config(config, BaseSeriesTransformer)


def setup_series_transformer(
    transformer: BaseSeriesTransformer | dict,
) -> BaseSeriesTransformer:
    r"""Set up a ``pandas.Series`` transformer.

    The transformer is instantiated from its configuration
    by using the ``BaseSeriesTransformer`` factory function.

    Args:
        transformer: Specifies a ``pandas.Series`` transformer or its
            configuration.

    Returns:
        An instantiated transformer.

    Example usage:

    ```pycon
    >>> from flamme.transformer.series import setup_series_transformer
    >>> transformer = setup_series_transformer(
    ...     {"_target_": "flamme.transformer.series.ToNumeric"}
    ... )
    >>> transformer
    ToNumericSeriesTransformer()

    ```
    """
    if isinstance(transformer, dict):
        logger.info("Initializing a series transformer from its configuration... ")
        transformer = BaseSeriesTransformer.factory(**transformer)
    if not isinstance(transformer, BaseSeriesTransformer):
        logger.warning(
            f"transformer is not a `BaseSeriesTransformer` (received: {type(transformer)})"
        )
    return transformer
