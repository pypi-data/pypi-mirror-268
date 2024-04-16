"""Corvic system data staging protocol."""

from typing import Protocol

import pyarrow as pa
import sqlglot


class StagingDB(Protocol):
    """A connection to some database where staging data can be found."""

    def count_ingested_rows(self, blob_name: str, *other_blob_names: str) -> int:
        """Returns the number of rows of the given blobs available for querying.

        Callers can expect this to be cheap to call.
        """
        ...

    def query_for_blobs(
        self, blob_names: list[str], column_names: list[str]
    ) -> sqlglot.exp.Query: ...

    def run_select_query(self, query: sqlglot.exp.Query) -> pa.RecordBatchReader: ...
