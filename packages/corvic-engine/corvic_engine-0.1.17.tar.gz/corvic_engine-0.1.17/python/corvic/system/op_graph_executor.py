"""Corvic system op graph executeor protocol."""

import dataclasses
from typing import Protocol

import pyarrow as pa

from corvic import op_graph


@dataclasses.dataclass
class ExecutionContext:
    """Description of the computation to be completed."""

    table_to_compute: op_graph.Op
    output_url_prefix: str


class OpGraphExecutionResult(Protocol):
    """Opaque container for the results of an execution."""

    def to_batch_reader(self) -> pa.RecordBatchReader:
        """Render the results as a stream of RecordBatches."""
        ...

    def to_urls(self) -> list[str]:
        """Render the results as a list of urls pointing to parquet files."""
        ...


class OpGraphExecutor(Protocol):
    """Execute table op graphs."""

    def execute(self, context: ExecutionContext) -> OpGraphExecutionResult:
        """Execute an op pgraph."""
        ...
