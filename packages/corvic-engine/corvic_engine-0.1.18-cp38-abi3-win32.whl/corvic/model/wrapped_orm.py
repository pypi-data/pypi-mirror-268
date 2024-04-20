"""Common model base."""

import abc
import dataclasses
from collections.abc import Iterable
from typing import Final, Generic, TypeVar

import sqlalchemy.orm as sa_orm
from typing_extensions import Self

from corvic import orm, system
from corvic.model.errors import InvalidOnAnonymousError

_ID = TypeVar(
    "_ID",
    orm.ResourceID,
    orm.SourceID,
    orm.SpaceID,
    orm.ExperimentID,
    orm.SpaceSourceID,
)
_OrmObj = TypeVar(
    "_OrmObj", orm.Resource, orm.Source, orm.Space, orm.Experiment, orm.SpaceSource
)


class WrappedOrmObject(Generic[_ID, _OrmObj], abc.ABC):
    """Base for orm wrappers providing a unified update mechanism."""

    _client: system.Client
    _orm_self: Final[_OrmObj]
    _derived_from_id: Final[_ID]

    def __init__(
        self,
        client: system.Client,
        orm_self: _OrmObj,
        derived_from_id: _ID,
    ):
        self._client = client
        self._orm_self = orm_self
        self._derived_from_id = derived_from_id

    def _make_id_from_orm(self, val: int | None) -> _ID:
        # this notation is a little awkward, we need _ID.from_orm() here, but
        # _ID is a TypeVar; This workaround accesses that classmethod through this
        # instance
        return self._derived_from_id.from_orm(val)

    @abc.abstractmethod
    def _make(self, orm_self: _OrmObj, derived_from_id: _ID) -> Self:
        """Children override this to pass additional  in to to __init__."""
        raise NotImplementedError()

    @abc.abstractmethod
    def _sub_orm_objects(self, orm_object: _OrmObj) -> Iterable[orm.Base]:
        raise NotImplementedError()

    @property
    def id(self) -> _ID:
        val = self._make_id_from_orm(self._orm_self.id)
        if not val:
            raise InvalidOnAnonymousError(
                "invalid request for the id of an unregistered object"
            )
        return val

    @property
    def derived_from_id(self) -> _ID:
        return self._derived_from_id

    @property
    def client(self) -> system.Client:
        return self._client

    def register(self) -> Self:
        """Assign this object a new ID by committing it to the database."""
        with sa_orm.Session(self.client.sa_engine, expire_on_commit=False) as session:
            new_orm_self = dataclasses.replace(self._orm_self, id=None)
            session.add(new_orm_self)
            for orm_object in self._sub_orm_objects(new_orm_self):
                session.add(orm_object)
            session.commit()

        return self._make(new_orm_self, self._make_id_from_orm(new_orm_self.id))

    def commit(self, id: _ID | None = None) -> Self:
        """Store this object in the database at the id, or derived_from_id.

        This overwrites the entry at id in the database so that future readers will see
        this object. One of `id` or `derived_from_id` cannot be empty or None.
        """
        with sa_orm.Session(self.client.sa_engine, expire_on_commit=False) as session:
            orm_id = (
                id.to_orm().unwrap_or_raise()
                if id
                else self.derived_from_id.to_orm().unwrap_or_raise()
            )
            new_orm_self = dataclasses.replace(self._orm_self, id=orm_id)
            session.merge(new_orm_self)
            session.commit()
        return self._make(new_orm_self, self._make_id_from_orm(new_orm_self.id))
