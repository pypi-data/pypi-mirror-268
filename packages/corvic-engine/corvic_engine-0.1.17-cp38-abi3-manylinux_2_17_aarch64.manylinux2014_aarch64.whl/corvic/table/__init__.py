"""Tabular data."""

# since these defs are in the public api for table, export them here
# as a convenience
from corvic.op_graph import FeatureType, RowFilter, feature_type, row_filter
from corvic.table.schema import Field, Schema
from corvic.table.table import (
    DataclassAsTypedMetadataMixin,
    MetadataValue,
    NotReadyError,
    Table,
    TypedMetadata,
)

__all__ = [
    "DataclassAsTypedMetadataMixin",
    "FeatureType",
    "Field",
    "MetadataValue",
    "NotReadyError",
    "RowFilter",
    "Schema",
    "Table",
    "TypedMetadata",
    "feature_type",
    "row_filter",
]
