r"""Contain some clickhouse utility functions."""

from __future__ import annotations

__all__ = ["get_table_schema", "get_dtypes"]


from typing import TYPE_CHECKING

import pyarrow as pa

from flamme.utils.dtype import get_dtypes_from_schema
from flamme.utils.path import sanitize_path

if TYPE_CHECKING:
    from pathlib import Path


def get_table_schema(path: Path | str) -> pa.Schema:
    r"""Return the table schema.

    Args:
        path: The path to the parquet file.

    Returns:
        The table schema.
    """
    return pa.parquet.read_schema(sanitize_path(path))


def get_dtypes(path: Path | str) -> dict[str, pa.DataType]:
    r"""Return the column data types from the schema.

    Args:
        path: The path to the schema.

    Returns:
        The mapping of column names and data types.
    """
    return get_dtypes_from_schema(schema=get_table_schema(path))
