r"""Contain the implementation of a simple ingestor."""

from __future__ import annotations

__all__ = ["Ingestor"]

from typing import TYPE_CHECKING

from flamme.ingestor.base import BaseIngestor

if TYPE_CHECKING:
    from pandas import DataFrame


class Ingestor(BaseIngestor):
    r"""Implement a simple DataFrame ingestor.

    Args:
        frame: The DataFrame to ingest.

    Example usage:

    ```pycon
    >>> import pandas as pd
    >>> from flamme.ingestor import Ingestor
    >>> ingestor = Ingestor(
    ...     frame=pd.DataFrame(
    ...         {
    ...             "col1": [1, 2, 3, 4, 5],
    ...             "col2": ["1", "2", "3", "4", "5"],
    ...             "col3": ["1", "2", "3", "4", "5"],
    ...             "col4": ["a", "b", "c", "d", "e"],
    ...         }
    ...     )
    ... )
    >>> ingestor
    Ingestor(shape=(5, 4))
    >>> frame = ingestor.ingest()

    ```
    """

    def __init__(self, frame: DataFrame) -> None:
        self._frame = frame

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}(shape={self._frame.shape})"

    def ingest(self) -> DataFrame:
        return self._frame
