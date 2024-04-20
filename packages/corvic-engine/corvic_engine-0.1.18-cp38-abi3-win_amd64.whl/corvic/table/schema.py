"""Corvic feature schemas."""

from __future__ import annotations

from collections.abc import Sequence
from typing import overload

import pyarrow as pa
from more_itertools import flatten

from corvic import orm
from corvic.op_graph import FeatureType, Op, feature_type, op
from corvic.result import BadArgumentError
from corvic_generated.orm.v1 import table_pb2


def _infer_possible_feature_types(  # noqa: PLR0911
    data_type: pa.DataType,
) -> Sequence[FeatureType]:
    if pa.types.is_integer(data_type):
        # TODO(thunt): Add multi-categorical in future versions
        return [
            feature_type.numerical(),
            feature_type.identifier(),
            feature_type.primary_key(),
            feature_type.categorical(),
            feature_type.foreign_key(referenced_source_id=orm.SourceID()),
            feature_type.unknown(),
        ]
    if pa.types.is_decimal(data_type) | pa.types.is_floating(data_type):
        return [
            feature_type.numerical(),
            feature_type.categorical(),
            feature_type.unknown(),
        ]
    if (
        pa.types.is_string(data_type)
        | pa.types.is_large_string(data_type)
        | pa.types.is_binary(data_type)
    ):
        # TODO(thunt): Add multi-categorical in future versions
        return [
            feature_type.text(),
            feature_type.identifier(),
            feature_type.primary_key(),
            feature_type.categorical(),
            feature_type.foreign_key(referenced_source_id=orm.SourceID()),
            feature_type.unknown(),
        ]
    if pa.types.is_boolean(data_type):
        # TODO(thunt): Add Numerical in future versions
        return [feature_type.categorical(), feature_type.unknown()]
    if pa.types.is_list(data_type):
        return [feature_type.embedding(), feature_type.unknown()]
    if pa.types.is_temporal(data_type):
        # TODO(thunt): Add Identifier, Primary Key, Foreign Key, Categorical in future
        # versions
        return [feature_type.timestamp(), feature_type.unknown()]
    return [feature_type.unknown()]


agg_mapping = {
    table_pb2.AGGREGATION_TYPE_COUNT: "count",
    table_pb2.AGGREGATION_TYPE_AVG: "avg",
    table_pb2.AGGREGATION_TYPE_MODE: "mode",
    table_pb2.AGGREGATION_TYPE_MIN: "min",
    table_pb2.AGGREGATION_TYPE_MAX: "max",
    table_pb2.AGGREGATION_TYPE_SUM: "sum",
}


def _generate_schema_for_rollup(
    schema: Schema,
    agg: table_pb2.AggregationType,
    group_by_column_names: Sequence[str],
    target_column_name: str,
) -> dict[str, Field]:
    new_fields: dict[str, Field] = {}
    group_by_str = "_".join(group_by_column_names)
    for field in schema:
        new_fields.update(
            {key: field for key in group_by_column_names if field.name == key}
        )
        if field.name == target_column_name:
            new_fields.update(
                {
                    f"{agg_mapping[agg]}_{target_column_name}_{group_by_str}": Field(
                        f"{agg_mapping[agg]}_{target_column_name}_{group_by_str}",
                        (
                            pa.uint32()
                            if agg_mapping[agg] == "count"
                            else (
                                pa.float32()
                                if agg_mapping[agg] == "avg"
                                else field.dtype
                            )
                        ),
                        (
                            feature_type.categorical()
                            if agg_mapping[agg] == "mode"
                            else feature_type.numerical()
                        ),
                    )
                }
            )
    return new_fields


class Field:
    """A named field, with a data type and feature type."""

    _name: str
    _dtype: pa.DataType
    _ftype: FeatureType

    def __init__(
        self,
        name: str,
        dtype: pa.DataType,
        ftype: FeatureType,
    ) -> None:
        self._name = name
        self._dtype = dtype
        self._ftype = ftype

    def __str__(self) -> str:
        """Legible string representation."""
        return f"{self._name}: {self._dtype}, {self._ftype}"

    def __eq__(self, other: object) -> bool:
        """Two fields are equal if their contents match."""
        if isinstance(other, Field):
            return (
                self._name == other._name
                and self._dtype == other._dtype
                and self._ftype == other._ftype
            )
        return False

    @property
    def dtype(self) -> pa.DataType:
        return self._dtype

    @property
    def name(self) -> str:
        return self._name

    @property
    def ftype(self) -> FeatureType:
        return self._ftype

    @classmethod
    def _decode_feature_type(cls, arrow_field: pa.Field) -> FeatureType:
        ftypes = _infer_possible_feature_types(arrow_field.type)
        if not ftypes:
            raise ValueError("No feature types detected.")
        return ftypes[0]

    @classmethod
    def from_arrow(
        cls,
        arrow_field: pa.Field,
        feature_type: FeatureType | None = None,
    ) -> Field:
        feature_type = feature_type or cls._decode_feature_type(arrow_field)
        return Field(
            arrow_field.name,
            arrow_field.type,
            feature_type,
        )

    def to_arrow(self) -> pa.Field:
        return pa.field(
            self.name,
            self.dtype,
        )

    def rename(self, new_name: str) -> Field:
        return Field(new_name, self.dtype, self.ftype)

    def possible_feature_types(self) -> Sequence[FeatureType]:
        """Infer possible feature types given the data type."""
        return _infer_possible_feature_types(self.dtype)


def _make_schema_from_node2vec_params(n2v_op: op.EmbedNode2vecFromEdgeLists):
    if not n2v_op.edge_list_tables:
        raise BadArgumentError("unable to infer schema: empty edge table list")

    first_table = n2v_op.edge_list_tables[0]
    first_table_schema = Schema.from_ops(first_table.table)
    output_dtype = first_table_schema[first_table.start_column_name].dtype
    if output_dtype != first_table_schema[first_table.end_column_name].dtype:
        raise BadArgumentError(
            "unable to infer schema: detected different output dtypes"
        )

    for edge_list_table in n2v_op.edge_list_tables[1:]:
        schema = Schema.from_ops(edge_list_table.table)
        start_column_dtype = schema[edge_list_table.start_column_name].dtype
        end_column_dtype = schema[edge_list_table.end_column_name].dtype
        if output_dtype != start_column_dtype or output_dtype != end_column_dtype:
            raise BadArgumentError(
                "unable to infer schema: detected different output dtypes"
            )

    return Schema(
        [
            Field(
                "id",
                pa.struct(
                    [
                        pa.field(name="column_0", type=output_dtype),
                        pa.field(name="column_1", type=pa.large_string()),
                    ]
                ),
                feature_type.identifier(),
            ),
            Field(
                "embedding",
                pa.list_(value_type=pa.float32(), list_size=n2v_op.ndim),
                feature_type.embedding(),
            ),
        ]
    )


def _make_schema_for_embedding_coordinates(op: op.EmbeddingCoordinates):
    schema = Schema.from_ops(op.table)

    if "id" not in schema or "embedding" not in schema:
        raise BadArgumentError(
            "EmbeddingMetrics op needs to be computed on Embedding table"
        )

    return Schema(
        [
            schema["id"],
            Field(
                "embedding",
                pa.list_(value_type=pa.float32(), list_size=3),
                feature_type.embedding(),
            ),
        ]
    )


class Schema(Sequence[Field]):
    """List of fields describing data types and feature types of a table."""

    _fields: list[Field]

    def __init__(self, fields: list[Field]) -> None:
        self._fields = fields

    def __eq__(self, other: object) -> bool:
        """Two schemas are equal if all of their fields match."""
        if isinstance(other, Schema):
            return self._fields == other._fields
        return False

    @overload
    def __getitem__(self, selection: str) -> Field: ...

    @overload
    def __getitem__(self, selection: int) -> Field: ...

    @overload
    def __getitem__(self, selection: slice) -> Sequence[Field]: ...

    def __getitem__(self, selection: int | str | slice) -> Field | Sequence[Field]:  # pyright: ignore[reportIncompatibleMethodOverride]
        """This operation is akin to pyarrow.Schema.field.

        The result is either the array addressed Field(s) or the first field with a
        matching name depending on the type of argument passed.
        """
        if isinstance(selection, str):
            for field in self._fields:
                if field.name == selection:
                    return field
            raise KeyError("no field with that name")
        return self._fields[selection]

    def __len__(self):
        """The number of fields in this schema."""
        return len(self._fields)

    def __str__(self) -> str:
        """Legible string representation of this schema."""
        return "\n".join(str(field) for field in self)

    def has_column(self, column_name: str) -> bool:
        return any(field.name == column_name for field in self)

    @classmethod
    def from_arrow(
        cls,
        arrow_schema: pa.Schema,
        feature_types: Sequence[FeatureType | None] | None = None,
    ) -> Schema:
        if feature_types:
            if len(feature_types) != len(arrow_schema):
                raise BadArgumentError("length of feature_types must match schema")
        else:
            feature_types = [None] * len(arrow_schema)
        return cls(
            fields=[
                Field.from_arrow(field, ftype)
                for field, ftype in zip(arrow_schema, feature_types, strict=True)
            ]
        )

    def to_arrow(self) -> pa.Schema:
        return pa.schema(field.to_arrow() for field in self)

    def get_primary_key(self) -> Field | None:
        for field in self:
            match field.ftype:
                case feature_type.PrimaryKey():
                    return field
                case _:
                    pass
        return None

    def get_foreign_keys(self, source_id: orm.SourceID) -> list[Field]:
        def generate_matching_fields():
            for field in self:
                match field.ftype:
                    case feature_type.ForeignKey(ref_id) if ref_id == source_id:
                        yield field
                    case _:
                        pass

        return list(generate_matching_fields())

    @classmethod
    def from_ops(cls, ops: Op) -> Schema:  # noqa: PLR0911
        match ops:
            case op.SelectFromStaging() | op.ReadFromParquet():
                return Schema(
                    [
                        Field.from_arrow(afield, ftype)
                        for afield, ftype in zip(
                            ops.arrow_schema, ops.feature_types, strict=True
                        )
                    ]
                )
            case op.SelectColumns():
                return Schema(
                    [
                        field
                        for field in cls.from_ops(ops.source)
                        if field.name in ops.columns
                    ]
                )
            case op.RenameColumns():

                def rename_column(field: Field) -> Field:
                    if field.name in ops.old_name_to_new:
                        return field.rename(ops.old_name_to_new[field.name])
                    return field

                return Schema(list(map(rename_column, cls.from_ops(ops.source))))

            case op.UpdateFeatureTypes():

                def update_feature_type(field: Field) -> Field:
                    if field.name in ops.new_feature_types:
                        return Field(
                            field.name, field.dtype, ops.new_feature_types[field.name]
                        )
                    return field

                return Schema(list(map(update_feature_type, cls.from_ops(ops.source))))

            case op.Join():
                left_schema = cls.from_ops(ops.left_source)
                right_schema = cls.from_ops(ops.right_source)
                left_names = {field.name for field in left_schema}
                return Schema(
                    list(
                        flatten(
                            (
                                (field for field in left_schema),
                                (
                                    field
                                    for field in right_schema
                                    if field.name not in left_names
                                    and field.name not in ops.right_join_columns
                                ),
                            )
                        )
                    )
                )

            case (
                op.LimitRows()
                | op.OrderBy()
                | op.FilterRows()
                | op.DistinctRows()
                | op.UpdateMetadata()
                | op.SetMetadata()
                | op.RemoveFromMetadata()
            ):
                return cls.from_ops(ops.source)

            case op.EmbeddingMetrics():
                return cls.from_ops(ops.table)

            case op.RollupByAggregation():
                schema = cls.from_ops(ops.source)
                new_fields = _generate_schema_for_rollup(
                    schema,
                    ops.aggregation_type,
                    ops.group_by_column_names,
                    ops.target_column_name,
                )
                return Schema(list(new_fields.values()))

            case op.Empty():
                return Schema([])

            case op.EmbedNode2vecFromEdgeLists():
                return _make_schema_from_node2vec_params(ops)

            case op.EmbeddingCoordinates():
                return _make_schema_for_embedding_coordinates(ops)
