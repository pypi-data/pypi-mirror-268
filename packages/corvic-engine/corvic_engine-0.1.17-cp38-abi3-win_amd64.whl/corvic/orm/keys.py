"""Helpers for dealing with model keys."""

import functools
from typing import TypeAlias

import sqlalchemy as sa
import sqlalchemy.orm as sa_orm

from corvic.result import Error

MappedPrimaryKey: TypeAlias = sa_orm.Mapped[int | None]
"""Type annotation for a primary key column.

Though primary keys are required and are not usually nullable, they are often assigned
by the database. Hence, they might be "None" sometimes, especially for objects that
have not yet been persisted.
"""

primary_key_column = functools.partial(
    sa_orm.mapped_column, primary_key=True, nullable=False, default=None
)
"""Primary key mapped column.

This sets the common options used by primary keys across models.
"""


class ForeignKey:
    """Factory class for producing foreign keys on corvic orm models."""

    class UnsupportedModelError(Error):
        """Error raised when foreign key cannot be generated for requested model."""

    def __init__(self, cls: type[sa_orm.DeclarativeBase]):
        self._model_mapper = sa.inspect(cls)
        if len(self.reference_table_primary_key_columns) != 1:
            raise self.UnsupportedModelError(
                "ForeignKey helper can only be used with models that have one primary "
                + "key and does not support tables with multi-column primary keys."
            )

    @property
    def model_mapper(self):
        return self._model_mapper

    @property
    def reference_table_primary_key_columns(self):
        return self.model_mapper.primary_key

    @property
    def reference_table_primary_key_column(self):
        return self.model_mapper.primary_key[0]

    @property
    def make(self):
        return functools.partial(sa.ForeignKey, self.reference_table_primary_key_column)
