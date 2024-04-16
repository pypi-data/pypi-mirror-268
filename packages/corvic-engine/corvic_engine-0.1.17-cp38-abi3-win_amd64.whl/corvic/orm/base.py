"""Base models for corvic RDBMS backed orm tables."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, ClassVar

import sqlalchemy as sa
import sqlalchemy.orm as sa_orm
from sqlalchemy.ext import hybrid

import corvic.result
from corvic.orm.func import gen_uuid, utc_now
from corvic.orm.keys import ForeignKey, primary_key_column


class Base(sa_orm.MappedAsDataclass, sa_orm.DeclarativeBase):
    """Base class for all DB mapped classes."""

    _created_at: sa_orm.Mapped[datetime] = sa_orm.mapped_column(
        "created_at", sa.DateTime, server_default=utc_now(), init=False
    )
    _updated_at: sa_orm.Mapped[datetime] = sa_orm.mapped_column(
        "updated_at",
        sa.DateTime,
        onupdate=utc_now(),
        server_default=utc_now(),
        init=False,
        nullable=True,
    )

    @hybrid.hybrid_property
    def created_at(self) -> datetime:
        if not self._created_at:
            # If not committed in the database the output should be None.
            # Align the typing to other fields without the None included.
            return None  # pyright: ignore[reportReturnType]
        return self._created_at.replace(tzinfo=timezone.utc)

    @hybrid.hybrid_property
    def updated_at(self) -> datetime:
        if not self._updated_at:
            # If not committed in the database the output should be None.
            # Align the typing to other fields without the None included.
            return None  # pyright: ignore[reportReturnType]
        return self._updated_at.replace(tzinfo=timezone.utc)

    @classmethod
    def foreign_key(cls):
        return ForeignKey(cls=cls)


class OrgBase(Base):
    """An organization it a top level grouping of resources."""

    __tablename__ = "org"

    # overriding table_args is the recommending way of defining these base model types
    __table_args__: ClassVar[Any] = ({"extend_existing": True},)

    id: sa_orm.Mapped[str | None] = primary_key_column(server_default=gen_uuid())

    @hybrid.hybrid_property
    def name(self) -> str:
        if self.id is None:
            raise corvic.result.Error(
                "invalid request for the id of an unregistered object"
            )
        return self.id
