"""Spaces."""

from __future__ import annotations

import dataclasses
import functools
from collections.abc import Iterable
from typing import Any, Final, TypeAlias

from more_itertools import flatten
from typing_extensions import Self

from corvic import orm, system
from corvic.model.defaults import get_default_client
from corvic.model.sources import Source, SourceID
from corvic.model.wrapped_orm import WrappedOrmObject
from corvic.result import BadArgumentError
from corvic.table import (
    DataclassAsTypedMetadataMixin,
    RowFilter,
    Table,
    feature_type,
    row_filter,
)

SpaceID: TypeAlias = orm.SpaceID
SpaceSourceID: TypeAlias = orm.SpaceID


class Column:
    """A logical representation of a column to use in filter predicates.

    Columns are identified by name.
    """

    _column_name: Final[str]

    def __init__(self, column_name: str):
        """Creates a new instance of Column.

        Args:
            column_name: Name of the column
        """
        self._column_name = column_name

    def eq(self, value: Any) -> RowFilter:
        """Return rows where column is equal to a value."""
        return row_filter.eq(column_name=self._column_name, literal=value)

    def ne(self, value: Any) -> RowFilter:
        """Return rows where column is not equal to a value."""
        return row_filter.ne(column_name=self._column_name, literal=value)

    def gt(self, value: Any) -> RowFilter:
        """Return rows where column is greater than a value."""
        return row_filter.gt(column_name=self._column_name, literal=value)

    def lt(self, value: Any) -> RowFilter:
        """Return rows where column is less than a value."""
        return row_filter.lt(column_name=self._column_name, literal=value)

    def ge(self, value: Any) -> RowFilter:
        """Return rows where column is greater than or equal to a value."""
        return row_filter.ge(column_name=self._column_name, literal=value)

    def le(self, value: Any) -> RowFilter:
        """Return rows where column is less than or equal to a value."""
        return row_filter.le(column_name=self._column_name, literal=value)

    def in_(self, value: list[Any]) -> RowFilter:
        """Return rows where column matches any in a list of values."""
        return row_filter.in_(column_name=self._column_name, literals=value)


@dataclasses.dataclass(frozen=True)
class FkeyRelationship:
    """A foreign key relationship between sources."""

    source_with_fkey: SourceID
    fkey_column_name: str
    referenced_source: SourceID
    pkey_column_name: str


@dataclasses.dataclass(frozen=True)
class Relationship:
    """A connection between two sources within a space."""

    from_source_id: SourceID
    to_source_id: SourceID
    space: Space

    fkey_relationship: FkeyRelationship

    @property
    def from_column_name(self) -> str:
        if self.from_source_id == self.fkey_relationship.source_with_fkey:
            return self.fkey_relationship.fkey_column_name
        return self.fkey_relationship.pkey_column_name

    @property
    def to_column_name(self) -> str:
        if self.to_source_id == self.fkey_relationship.source_with_fkey:
            return self.fkey_relationship.fkey_column_name
        return self.fkey_relationship.pkey_column_name

    @property
    def new_column_name(self) -> str:
        return self.fkey_relationship.fkey_column_name

    @property
    def from_space_source(self):
        return self.space.get_space_source(self.from_source_id)

    @property
    def to_space_source(self):
        return self.space.get_space_source(self.to_source_id)

    def joined_table(self) -> Table:
        start_table = self.from_space_source.table.rename_columns(
            {self.from_column_name: self.new_column_name}
        )
        end_table = self.to_space_source.table.rename_columns(
            {self.to_column_name: self.new_column_name}
        )

        return start_table.join(
            end_table,
            left_on=self.new_column_name,
            right_on=self.new_column_name,
            how="inner",
        )

    def edge_list(self) -> Iterable[tuple[Any, Any]]:
        start_pk = self.from_space_source.table.schema.get_primary_key()
        end_pk = self.to_space_source.table.schema.get_primary_key()

        if not start_pk or not end_pk:
            raise BadArgumentError(
                "both sources must have a primary key to render edge list"
            )

        if self.from_column_name == start_pk.name:
            result_columns = (self.new_column_name, end_pk.name)
        else:
            result_columns = (start_pk.name, self.new_column_name)

        result = self.joined_table().select(result_columns)

        for batch in result.to_polars().unwrap_or_raise():
            for row in batch.rows(named=True):
                yield (row[result_columns[0]], row[result_columns[1]])


class SpaceSource(WrappedOrmObject[SpaceSourceID, orm.SpaceSource]):
    """A table from a source with some extra operations defined by a space."""

    _source: Final[Source]

    def __init__(
        self,
        client: system.Client,
        orm_self: orm.SpaceSource,
        derived_from_id: SpaceSourceID,
        source: Source | None = None,
    ):
        super().__init__(client, orm_self, derived_from_id)
        if source is None:
            if not orm_self.source_id:
                raise BadArgumentError("could not determine the source")
            source = Source.from_id(
                SourceID.from_orm(orm_self.source_id), self.client
            ).unwrap_or_raise()
        self._source = source

    def _sub_orm_objects(self, orm_object: orm.SpaceSource) -> Iterable[orm.Base]:
        _ = (orm_object,)
        return []

    def _make(self, orm_self: orm.SpaceSource, derived_from_id: SpaceSourceID) -> Self:
        return type(self)(self.client, orm_self, derived_from_id, self._source)

    @functools.cached_property
    def table(self):
        return Table.from_bytes(self.client, self._orm_self.table_op_graph)

    @property
    def source(self):
        return self._source


@dataclasses.dataclass(kw_only=True)
class SpaceEdgeTableMetadata(DataclassAsTypedMetadataMixin):
    """Metadata attached to edge tables; notes important columns and provenance."""

    @classmethod
    def metadata_key(cls):
        return "space-edge_table-metadata"

    start_source_name: str
    end_source_name: str
    start_source_column_name: str
    end_source_column_name: str


class Space(WrappedOrmObject[SpaceID, orm.Space]):
    """Spaces describe how Sources should be modeled to create a feature space.

    Example:
    >>> Space.create()
    >>>    .with_entity(
    >>>        customer_source.id,
    >>>        row_filter=Column("customer_name").eq("Denis").or_(Column("id").lt(3)),
    >>>        drop_disconnected=True,
    >>>    )
    >>>    .with_entity(
    >>>        order_source,
    >>>        include_columns=["id", "ordered_item"],
    >>>    )
    >>>    .wth_relationship(customer_source.id, order_source.id, directional=False)
    """

    _space_sources: Final[dict[SourceID, SpaceSource]]
    _relationships: Final[list[Relationship]]
    _output_sources: Final[set[SourceID]]

    def __init__(
        self,
        client: system.Client,
        orm_self: orm.Space,
        derived_from_id: SpaceID,
        space_sources: dict[SourceID, SpaceSource],
        relationships: list[Relationship],
        output_sources: set[SourceID],
    ):
        super().__init__(client, orm_self, derived_from_id)
        self._space_sources = space_sources
        self._relationships = [
            dataclasses.replace(rel, space=self) for rel in relationships
        ]
        self._output_sources = output_sources

    def _make(self, orm_self: orm.Space, derived_from_id: SpaceID) -> Self:
        return type(self)(
            self.client,
            orm_self,
            derived_from_id,
            self._space_sources,
            self._relationships,
            self._output_sources,
        )

    def _sub_orm_objects(self, orm_object: orm.Space) -> Iterable[orm.Base]:
        _ = (orm_object,)
        return []

    @property
    def relationships(self) -> list[Relationship]:
        return list(self._relationships)

    def _calculate_paths_to_outputs(self, output: SourceID, rels: list[Relationship]):
        paths: list[list[Relationship]] = []
        for rel in rels:
            if rel.from_source_id == output:
                if rel.to_source_id in self._output_sources:
                    paths.append([rel])
                else:
                    child_paths = self._calculate_paths_to_outputs(
                        rel.to_source_id,
                        [  # we only want to use a fkey relationship once per path
                            next_rel
                            for next_rel in rels
                            if next_rel.fkey_relationship != rel.fkey_relationship
                        ],
                    )
                    paths.extend([rel, *child_path] for child_path in child_paths)
        return paths

    @staticmethod
    def _find_source_dest_columns(rels: list[Relationship]) -> tuple[str, str]:
        # source is the new column if new_column and to_column match because it was
        # the foreign key, else it's the primary key of the from_source
        if rels[0].new_column_name == rels[0].to_column_name:
            source = rels[0].new_column_name
        else:
            pk = rels[0].from_space_source.table.schema.get_primary_key()
            source = pk.name if pk else ""
        if rels[-1].new_column_name == rels[-1].from_column_name:
            dest = rels[-1].new_column_name
        else:
            pk = rels[0].to_space_source.table.schema.get_primary_key()
            dest = pk.name if pk else ""

        return (source, dest)

    def output_edge_tables(self) -> list[Table]:
        paths_between_outputs = list(
            flatten(
                self._calculate_paths_to_outputs(output, self.relationships)
                for output in self._output_sources
            )
        )
        edge_tables = list[Table]()
        for path in paths_between_outputs:
            path_itr = iter(path)
            rel = next(path_itr)
            table = rel.joined_table()
            for rel in path_itr:
                table = table.rename_columns(
                    {rel.from_column_name: rel.new_column_name}
                ).join(
                    rel.to_space_source.table.rename_columns(
                        {rel.to_column_name: rel.new_column_name}
                    ),
                    left_on=rel.new_column_name,
                    right_on=rel.new_column_name,
                )
            source_col, dest_col = self._find_source_dest_columns(path)
            table = table.update_typed_metadata(
                SpaceEdgeTableMetadata(
                    start_source_name=path[0].from_space_source.source.name,
                    end_source_name=path[-1].to_space_source.source.name,
                    start_source_column_name=source_col,
                    end_source_column_name=dest_col,
                )
            )
            edge_tables.append(table)
        return edge_tables

    @classmethod
    def create(cls, client: system.Client | None = None) -> Space:
        """Create a Space."""
        orm_space = orm.Space()
        client = client or get_default_client()
        return Space(
            client,
            orm_space,
            SpaceID(),
            space_sources={},
            relationships=[],
            output_sources=set(),
        )

    def get_space_source(self, source_id: SourceID) -> SpaceSource:
        return self._space_sources[source_id]

    @property
    def space_sources(self) -> list[SpaceSource]:
        return list(self._space_sources.values())

    def with_source(
        self,
        source_id: SourceID,
        *,
        row_filter: RowFilter | None = None,
        drop_disconnected: bool = False,
        include_columns: list[str] | None = None,
        output: bool = False,
    ) -> Space:
        """Define a source to be considered in Space.

        Args:
            source_id: The if of the source to be considered in the space
            row_filter: Row level filters to be applied on source
            drop_disconnected: Filter orphan nodes in source
            include_columns: Column level filters to be applied on source
            output: Set to True if this should should be an entity in the ourput

        Example:
        >>> with_entity(
        >>>     customer_source_id,
        >>>     row_filter=Column("customer_name").eq("Denis"),
        >>>     drop_disconnected=True,
        >>>     include_columns=["id", "customer_name"],
        >>> )
        """
        # TODO(thunt): Reminder that these new table ops should start
        # from loading the source
        source = Source.from_id(source_id, self.client).unwrap_or_raise()
        new_table = source.table
        if row_filter:
            new_table = new_table.filter_rows(row_filter)
        if include_columns:
            new_table = new_table.select(include_columns)

        orm_space_source = orm.SpaceSource(
            table_op_graph=new_table.op_graph.to_bytes(),
            drop_disconnected=drop_disconnected,
        )

        space_sources = self._space_sources.copy()
        space_sources.update(
            {
                source.id: SpaceSource(
                    self.client, orm_space_source, SpaceSourceID(), source
                )
            }
        )

        output_sources = self._output_sources
        if output:
            primary_key = source.table.schema.get_primary_key()
            if not primary_key:
                raise BadArgumentError(
                    "source must have a primary key to part of the output"
                )
            output_sources = output_sources.union({source.id})

        return Space(
            self.client,
            dataclasses.replace(self._orm_self, id=None),
            derived_from_id=self.derived_from_id,
            space_sources=space_sources,
            relationships=self._relationships,
            output_sources=output_sources,
        )

    def _check_or_infer_foreign_keys(  # noqa: C901
        self,
        from_source_id: SourceID,
        to_source_id: SourceID,
        from_foreign_key: str | None,
        to_foreign_key: str | None,
    ) -> tuple[str | None, str | None]:
        frm = self._space_sources[from_source_id]
        to = self._space_sources[to_source_id]

        if from_foreign_key:
            match frm.table.schema[from_foreign_key].ftype:
                case feature_type.ForeignKey(referenced_source_id):
                    if referenced_source_id != to.source.id:
                        raise BadArgumentError(
                            "from_foreign_key does not reference to_source_id",
                            to_source_id=str(to.source.id),
                            referenced_source_id=str(referenced_source_id),
                        )
                case _:
                    raise BadArgumentError(
                        "the provided from_foreign_key is not a ForeignKey feature"
                    )

        if to_foreign_key:
            match to.table.schema[to_foreign_key].ftype:
                case feature_type.ForeignKey(referenced_source_id):
                    if referenced_source_id != frm.source.id:
                        raise BadArgumentError(
                            "to_foreign_key does not reference from_source_id",
                            from_source_id=str(frm.source.id),
                            referenced_source_id=str(referenced_source_id),
                        )
                case _:
                    raise BadArgumentError(
                        "the provided to_foreign_key is not a ForeignKey feature"
                    )

        if not from_foreign_key and not to_foreign_key:
            from_foreign_keys = [
                field.name for field in frm.table.schema.get_foreign_keys(to.source.id)
            ]
            to_foreign_keys = [
                field.name for field in to.table.schema.get_foreign_keys(frm.source.id)
            ]

            if (
                (from_foreign_keys and to_foreign_keys)
                or len(from_foreign_keys) > 1
                or len(to_foreign_keys) > 1
            ):
                raise BadArgumentError(
                    "relationship is ambiguous:"
                    + "provide from_foreign_key or to_foreign_key to disambiguate",
                    from_foreign_keys=from_foreign_keys,
                    to_foreign_keys=to_foreign_keys,
                )
            if from_foreign_keys:
                from_foreign_key = from_foreign_keys[0]
            if to_foreign_keys:
                to_foreign_key = to_foreign_keys[0]

        return (from_foreign_key, to_foreign_key)

    def with_all_implied_relationships(self) -> Space:
        """Automatically define non-directional relationships based on foreign keys."""
        new_space = self
        for space_source in self.space_sources:
            for field in space_source.source.table.schema:
                match field.ftype:
                    case feature_type.ForeignKey(referenced_source_id):
                        # We don't know the intended direction, add both directions
                        new_space = new_space.with_relationship(
                            referenced_source_id,
                            space_source.source.id,
                            to_foreign_key=field.name,
                            directional=False,
                        )
                    case _:
                        pass
        return new_space

    def with_relationship(
        self,
        from_source_id: SourceID,
        to_source_id: SourceID,
        *,
        from_foreign_key: str | None = None,
        to_foreign_key: str | None = None,
        directional: bool = False,
    ) -> Space:
        """Define relationship between two sources.

        Args:
            from_source_id: The ID of the source on the "from" side (if dircectional)
            to_source_id: The ID of the source on the "to" side (if dircectional)
            from_foreign_key: The foreign key to use to match on the "from"
                source. Required if there is more than one foreign key relationship
                linking the sources. Cannot be used with "to_foreign_key".
            to_foreign_key: The foreign key to use to match on the "to"
                source. Required if there is more than one foreign key relationship
                linking the sources. Cannot be used with "from_foreign_key"
            directional: Whether to load graph as directional

        Example:
        >>> with_relationship(customer_source.id, order_source.id, directional=False)
        """
        if from_source_id not in self._space_sources:
            raise BadArgumentError(
                "from_source_id does not match any source in this space",
                from_source_id=str(from_source_id),
            )
        if to_source_id not in self._space_sources:
            raise BadArgumentError(
                "to_source_id does not match any source in this space",
                to_source_id=str(to_source_id),
            )

        if from_foreign_key and to_foreign_key:
            raise BadArgumentError(
                "only one of from_foreign_key and to_foreign_key may be provided",
                to_source_id=str(to_source_id),
            )

        from_foreign_key, to_foreign_key = self._check_or_infer_foreign_keys(
            from_source_id, to_source_id, from_foreign_key, to_foreign_key
        )

        if from_foreign_key:
            pk = self._space_sources[to_source_id].table.schema.get_primary_key()
            if not pk:
                raise BadArgumentError(
                    "source has no primary key, "
                    + "so it cannot be referenced by foreign key",
                    from_source_id=str(from_source_id),
                )

            fkey_relationship = FkeyRelationship(
                source_with_fkey=from_source_id,
                fkey_column_name=from_foreign_key,
                referenced_source=to_source_id,
                pkey_column_name=pk.name,
            )
        elif to_foreign_key:
            pk = self._space_sources[from_source_id].table.schema.get_primary_key()
            if not pk:
                raise BadArgumentError(
                    "source has no primary key, "
                    + "so it cannot be referenced by foreign key",
                    to_source_id=str(to_source_id),
                )
            fkey_relationship = FkeyRelationship(
                source_with_fkey=to_source_id,
                fkey_column_name=to_foreign_key,
                referenced_source=from_source_id,
                pkey_column_name=pk.name,
            )
        else:
            raise BadArgumentError(
                "foreign key relationship was not provided and could not be inferred"
            )

        relationships = [dataclasses.replace(val) for val in self._relationships]

        relationships.append(
            Relationship(
                from_source_id=from_source_id,
                to_source_id=to_source_id,
                space=self,
                fkey_relationship=fkey_relationship,
            )
        )
        if not directional:
            relationships.append(
                Relationship(
                    from_source_id=to_source_id,
                    to_source_id=from_source_id,
                    space=self,
                    fkey_relationship=fkey_relationship,
                )
            )

        return Space(
            self.client,
            dataclasses.replace(self._orm_self, id=None),
            derived_from_id=self.derived_from_id,
            space_sources=self._space_sources,
            relationships=relationships,
            output_sources=self._output_sources,
        )
