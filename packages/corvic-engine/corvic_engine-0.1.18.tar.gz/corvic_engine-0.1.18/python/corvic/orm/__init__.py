"""Data model definitions; backed by an RDBMS."""

from __future__ import annotations

from dataclasses import InitVar

import sqlalchemy as sa
from sqlalchemy import orm as sa_orm
from sqlalchemy.ext import hybrid
from sqlalchemy.orm.collections import attribute_mapped_collection

from corvic.orm.base import Base, OrgBase
from corvic.orm.errors import (
    DeletedObjectError,
    InvalidORMIdentifierError,
    RequestedObjectsForNobodyError,
)
from corvic.orm.ids import (
    ExperimentID,
    ExperimentRunID,
    OrgID,
    ResourceID,
    RoomID,
    SourceID,
    SpaceID,
    SpaceSourceID,
)
from corvic.orm.keys import MappedPrimaryKey, primary_key_column
from corvic.orm.mixins import BelongsToOrgMixin, Session, SoftDeleteMixin
from corvic_generated.feature.v1 import space_pb2


class Org(SoftDeleteMixin, OrgBase):
    """An organization it a top level grouping of resources."""

    rooms: sa_orm.Mapped[dict[str, Room]] = sa_orm.relationship(
        collection_class=attribute_mapped_collection("room_key"),
        cascade="all",
        init=False,
        default_factory=dict,
    )
    sources: sa_orm.Mapped[list[Source]] = sa_orm.relationship(
        collection_class=list, cascade="all", init=True, default_factory=list
    )

    def __init__(self, name: str | None = None):
        self.id = name


class Room(BelongsToOrgMixin, SoftDeleteMixin, Base):
    """A Room is a logical collection of Documents."""

    __tablename__ = "room"
    __table_args__ = (sa.UniqueConstraint("name", "org_id"),)

    name: sa_orm.Mapped[str] = sa_orm.mapped_column(sa.Text, default=None)
    id: MappedPrimaryKey = primary_key_column()
    org: sa_orm.Mapped[Org] = sa_orm.relationship(back_populates="rooms", init=False)

    spaces: sa_orm.Mapped[dict[str, Space]] = sa_orm.relationship(
        collection_class=attribute_mapped_collection("space_key"),
        cascade="all",
        init=False,
        default_factory=dict,
    )
    sources: sa_orm.Mapped[dict[str, Source]] = sa_orm.relationship(
        collection_class=attribute_mapped_collection("source_key"),
        cascade="all",
        init=False,
        default_factory=dict,
    )
    experiments: sa_orm.Mapped[dict[str, Experiment]] = sa_orm.relationship(
        collection_class=attribute_mapped_collection("experiment_key"),
        cascade="all",
        init=False,
        default_factory=dict,
    )

    @property
    def room_key(self):
        return self.name


class DefaultObjects(Base):
    """Holds the identifiers for default objects."""

    __tablename__ = "default_objects"
    default_org: sa_orm.Mapped[str] = sa_orm.mapped_column(
        Org.foreign_key().make(ondelete="CASCADE")
    )
    default_room: sa_orm.Mapped[int | None] = sa_orm.mapped_column(
        Room.foreign_key().make(ondelete="CASCADE"), nullable=True, default=None
    )
    version: MappedPrimaryKey = primary_key_column()


class Resource(BelongsToOrgMixin, Base):
    """A Resource is a reference to some durably stored file.

    E.g., a document could be a PDF file, an image, or a text transcript of a
    conversation
    """

    __tablename__ = "resource"

    name: sa_orm.Mapped[str] = sa_orm.mapped_column(sa.Text)
    mime_type: sa_orm.Mapped[str] = sa_orm.mapped_column(sa.Text)
    url: sa_orm.Mapped[str] = sa_orm.mapped_column(sa.Text)
    room_id: sa_orm.Mapped[int] = sa_orm.mapped_column(
        Room.foreign_key().make(ondelete="CASCADE"), name="room_id"
    )
    md5: sa_orm.Mapped[str] = sa_orm.mapped_column(sa.CHAR(32), nullable=True)
    size: sa_orm.Mapped[int] = sa_orm.mapped_column(nullable=True)
    original_path: sa_orm.Mapped[str] = sa_orm.mapped_column(nullable=True)
    description: sa_orm.Mapped[str] = sa_orm.mapped_column(nullable=True)
    id: MappedPrimaryKey = primary_key_column()

    source_associations: sa_orm.Mapped[list[SourceResourceAssociation]] = (
        sa_orm.relationship(
            back_populates="resource",
            cascade="save-update, merge, delete, delete-orphan",
            default_factory=list,
        )
    )


class Source(BelongsToOrgMixin, Base):
    """A source."""

    __tablename__ = "source"
    __table_args__ = (sa.UniqueConstraint("name", "room_id"),)

    name: sa_orm.Mapped[str] = sa_orm.mapped_column(sa.Text)
    room_id: sa_orm.Mapped[int] = sa_orm.mapped_column(
        Room.foreign_key().make(ondelete="CASCADE"),
    )
    # protobuf describing the operations required to construct a table
    table_op_graph: sa_orm.Mapped[bytes] = sa_orm.mapped_column(sa.LargeBinary)
    id: MappedPrimaryKey = primary_key_column()

    resource_associations: sa_orm.Mapped[list[SourceResourceAssociation]] = (
        sa_orm.relationship(
            back_populates="source",
            cascade="save-update, merge, delete, delete-orphan",
            default_factory=list,
        )
    )
    org: sa_orm.Mapped[Org] = sa_orm.relationship(back_populates="sources", init=False)
    room: sa_orm.Mapped[Room] = sa_orm.relationship(
        back_populates="sources", init=False
    )

    @property
    def source_key(self):
        return self.name


class SourceResourceAssociation(BelongsToOrgMixin, Base):
    __tablename__ = "source_resource_association"

    source_id: MappedPrimaryKey = (
        # this should be legal but pyright complains that it makes Source depend
        # on itself
        primary_key_column(Source.foreign_key().make())  # pyright: ignore[reportGeneralTypeIssues]
    )
    resource_id: MappedPrimaryKey = (
        # this should be legal but pyright complains that it makes Resource depend
        # on itself
        primary_key_column(Resource.foreign_key().make())  # pyright: ignore[reportGeneralTypeIssues]
    )
    source: sa_orm.Mapped[Source] = sa_orm.relationship(
        back_populates="resource_associations", init=False
    )
    resource: sa_orm.Mapped[Resource] = sa_orm.relationship(
        back_populates="source_associations", init=False
    )


class Space(SoftDeleteMixin, BelongsToOrgMixin, Base):
    """A Space is a logical collection of sources used by various experiments."""

    __tablename__ = "space"
    __table_args__ = (sa.UniqueConstraint("name", "room_id"),)

    id: MappedPrimaryKey = primary_key_column()
    name: sa_orm.Mapped[str] = sa_orm.mapped_column(sa.Text, default=None)
    description: sa_orm.Mapped[str] = sa_orm.mapped_column(sa.Text, default="")

    room_id: sa_orm.Mapped[int] = sa_orm.mapped_column(
        Room.foreign_key().make(ondelete="CASCADE"),
        nullable=True,
        init=True,
        default=None,
    )
    room: sa_orm.Mapped[Room] = sa_orm.relationship(back_populates="spaces", init=False)

    @property
    def space_key(self):
        return self.name

    space_sources: sa_orm.Mapped[list[SpaceSource]] = sa_orm.relationship(
        viewonly=True,
        init=True,
        default_factory=list,
        secondary="space_source",
        secondaryjoin=lambda: (Space.id == SpaceSource.space_id)
        & (SpaceSource.source_id == Source.id),
    )

    experiment_parameters: sa_orm.Mapped[list[ExperimentParameters]] = (
        sa_orm.relationship(
            viewonly=True,
            collection_class=list,
            cascade="all",
            init=False,
            secondary="experiment_parameters",
            default_factory=list,
            secondaryjoin=lambda: ExperimentParameters.space_id == Space.id,
        )
    )

    _space_output: sa_orm.Mapped[bytes | None] = sa_orm.mapped_column(
        sa.LargeBinary,
        init=False,
        nullable=True,
        server_default=sa.TextClause("NULL"),
    )
    initial_space_output: InitVar[space_pb2.SpaceOutput] = space_pb2.SpaceOutput()

    def __post_init__(self, initial_space_output: space_pb2.SpaceOutput):
        self._space_output = initial_space_output.SerializeToString()

    @hybrid.hybrid_property
    def space_output(self) -> space_pb2.SpaceOutput:
        if self._space_output:
            return space_pb2.SpaceOutput.FromString(self._space_output)
        return space_pb2.SpaceOutput()

    @space_output.inplace.setter
    def _update_space_output(self, value: space_pb2.SpaceOutput) -> None:
        self._space_output = value.SerializeToString()


class SpaceSource(BelongsToOrgMixin, Base):
    """Sources inside of a space."""

    __tablename__ = "space_source"
    table_op_graph: sa_orm.Mapped[bytes] = sa_orm.mapped_column(sa.LargeBinary)
    id: MappedPrimaryKey = primary_key_column()
    drop_disconnected: sa_orm.Mapped[bool] = sa_orm.mapped_column(default=False)
    space_id: sa_orm.Mapped[int] = sa_orm.mapped_column(
        Space.foreign_key().make(ondelete="CASCADE"), nullable=False, default=None
    )
    # this should be legal but pyright complains that it makes Source depend
    # on itself
    source_id: sa_orm.Mapped[int] = sa_orm.mapped_column(
        Source.foreign_key().make(ondelete="CASCADE"),  # pyright: ignore[reportGeneralTypeIssues]
        nullable=False,
        default=None,
    )
    source: sa_orm.Mapped[Source] = sa_orm.relationship(init=True, default=None)
    space: sa_orm.Mapped[Space] = sa_orm.relationship(init=True, default=None)


class Experiment(BelongsToOrgMixin, Base):
    """An experiment is a named evaluation of experiment parameters."""

    __tablename__ = "experiment"
    __table_args__ = (sa.UniqueConstraint("name", "room_id"),)

    table_op_graph: sa_orm.Mapped[bytes] = sa_orm.mapped_column(sa.LargeBinary)
    room_id: sa_orm.Mapped[int] = sa_orm.mapped_column(
        Room.foreign_key().make(ondelete="CASCADE"),
        nullable=True,
        init=True,
        default=None,
    )
    room: sa_orm.Mapped[Room] = sa_orm.relationship(
        back_populates="experiments", init=True, default=None
    )

    id: MappedPrimaryKey = primary_key_column()
    name: sa_orm.Mapped[str] = sa_orm.mapped_column(sa.Text, default=None)
    description: sa_orm.Mapped[str] = sa_orm.mapped_column(sa.Text, default="")
    parameters: sa_orm.Mapped[list[ExperimentParameters]] = sa_orm.relationship(
        viewonly=True,
        init=True,
        default_factory=list,
        secondary="experiment_parameters",
        secondaryjoin=lambda: (Experiment.id == ExperimentParameters.experiment_id),
    )

    @property
    def experiment_key(self):
        return self.name


class ExperimentParameters(BelongsToOrgMixin, Base):
    """Parameters for an experiment."""

    __tablename__ = "experiment_parameters"

    id: MappedPrimaryKey = primary_key_column()
    parameters: sa_orm.Mapped[bytes] = sa_orm.mapped_column(
        sa.LargeBinary, default=None
    )

    experiment_id: sa_orm.Mapped[int] = sa_orm.mapped_column(
        Experiment.foreign_key().make(ondelete="CASCADE"), nullable=False, default=None
    )
    experiment: sa_orm.Mapped[Experiment] = sa_orm.relationship(init=True, default=None)

    space_id: sa_orm.Mapped[int] = sa_orm.mapped_column(
        Space.foreign_key().make(ondelete="CASCADE"), nullable=False, default=None
    )
    space: sa_orm.Mapped[Space] = sa_orm.relationship(init=True, default=None)


class ExperimentRun(BelongsToOrgMixin, Base):
    """An Experiment run."""

    __tablename__ = "experiment_run"

    id: MappedPrimaryKey = primary_key_column()
    table_op_graph: sa_orm.Mapped[bytes] = sa_orm.mapped_column(
        sa.LargeBinary, default=b""
    )
    experiment_id: sa_orm.Mapped[int] = sa_orm.mapped_column(
        Experiment.foreign_key().make(ondelete="CASCADE"), nullable=False, default=None
    )
    experiment: sa_orm.Mapped[Experiment] = sa_orm.relationship(init=True, default=None)
    result_url: sa_orm.Mapped[str | None] = sa_orm.mapped_column(sa.Text, default=None)
    coordinates_url: sa_orm.Mapped[str | None] = sa_orm.mapped_column(
        sa.Text, default=None
    )
    is_running: sa_orm.Mapped[bool | None] = sa_orm.mapped_column(default=None)


__all__ = [
    "Base",
    "DefaultObjects",
    "DeletedObjectError",
    "Experiment",
    "ExperimentID",
    "ExperimentParameters",
    "ExperimentRun",
    "ExperimentRunID",
    "InvalidORMIdentifierError",
    "Org",
    "OrgID",
    "OrgID",
    "RequestedObjectsForNobodyError",
    "Resource",
    "ResourceID",
    "Room",
    "RoomID",
    "Session",
    "Source",
    "SourceID",
    "Space",
    "SpaceID",
    "SpaceSource",
    "SpaceSourceID",
]
