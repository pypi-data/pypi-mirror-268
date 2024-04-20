r"""Contain the implementation of a clickhouse ingestor."""

from __future__ import annotations

__all__ = ["ClickHouseIngestor"]

import logging
from typing import TYPE_CHECKING

from flamme.ingestor.base import BaseIngestor
from flamme.utils import setup_object

if TYPE_CHECKING:
    from flamme.utils.imports import is_clickhouse_connect_available

    if is_clickhouse_connect_available():
        import clickhouse_connect
    from pandas import DataFrame


logger = logging.getLogger(__name__)


class ClickHouseIngestor(BaseIngestor):
    r"""Implement a clickhouse DataFrame ingestor.

    Args:
        query: The query to get the data.
        client: The clickhouse client or its configuration.
            Please check the documentation of
            ``clickhouse_connect.get_client`` to get more information.

    Example usage:

    ```pycon
    >>> from flamme.ingestor import ClickHouseIngestor
    >>> import clickhouse_connect
    >>> client = clickhouse_connect.get_client()  # doctest: +SKIP
    >>> ingestor = ClickHouseIngestor(query="", client=client)  # doctest: +SKIP
    >>> frame = ingestor.ingest()  # doctest: +SKIP

    ```
    """

    def __init__(self, query: str, client: clickhouse_connect.driver.Client | dict) -> None:
        self._query = str(query)
        self._client: clickhouse_connect.driver.Client = setup_object(client)

    def __repr__(self) -> str:
        return f"{self.__class__.__qualname__}()"

    def ingest(self) -> DataFrame:
        logger.info(
            f"Ingesting data from clickhouse... \n\n"
            "---------------------------------------------------------------------------------\n"
            f"query:\n{self._query}\n"
            "---------------------------------------------------------------------------------\n\n"
        )
        frame = self._client.query_frame(query=self._query).sort_index(axis=1)
        logger.info(f"Data ingested. DataFrame shape: {frame.shape}")
        logger.info(f"number of unique column names: {len(set(frame.columns)):,}")
        return frame
