r"""Contain the implementation of a parquet schema reader."""

from __future__ import annotations

__all__ = ["ParquetSchemaReader"]

import logging
from typing import TYPE_CHECKING

from pyarrow.parquet import read_schema

from flamme.schema.reader.base import BaseSchemaReader
from flamme.utils.path import sanitize_path

if TYPE_CHECKING:
    from pathlib import Path

    import pyarrow as pa

logger = logging.getLogger(__name__)


class ParquetSchemaReader(BaseSchemaReader):
    r"""Implement a parquet schema reader.

    Args:
        path: The path to the parquet file to ingest.

    Example usage:

    ```pycon

    >>> import tempfile
    >>> import pandas as pd
    >>> from pathlib import Path
    >>> from flamme.schema.reader import ParquetSchemaReader
    >>> with tempfile.TemporaryDirectory() as tmpdir:
    ...     path = Path(tmpdir).joinpath("data.parquet")
    ...     pd.DataFrame({"col1": [1, 2, 3], "col2": ["a", "b", "c"]}).to_parquet(
    ...         path, index=False
    ...     )
    ...     reader = ParquetSchemaReader(path)
    ...     reader
    ...     schema = reader.read()
    ...     schema
    ...
    ParquetSchemaReader(path=.../data.parquet)
    col1: int64
    col2: string
    ...

    ```
    """

    def __init__(self, path: Path | str) -> None:
        self._path = sanitize_path(path)

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}(path={self._path})"

    def read(self) -> pa.Schema:
        logger.info(f"reading the schema from parquet file {self._path}...")
        schema = read_schema(self._path)
        logger.info("schema read")
        return schema
