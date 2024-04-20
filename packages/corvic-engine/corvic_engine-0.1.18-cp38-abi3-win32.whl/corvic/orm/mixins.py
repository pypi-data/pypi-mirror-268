"""Mixin models for corvic orm tables."""

from __future__ import annotations

from collections.abc import Callable
from datetime import datetime, timezone
from typing import Any, cast

import sqlalchemy as sa
from sqlalchemy import event, exc
from sqlalchemy import orm as sa_orm
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import UOWTransaction

import corvic.context
from corvic.orm.base import OrgBase
from corvic.orm.errors import DeletedObjectError, RequestedObjectsForNobodyError
from corvic.orm.ids import OrgID
from corvic.result import BadArgumentError


def _filter_org_objects(orm_execute_state: sa_orm.ORMExecuteState):
    if all(
        not issubclass(mapper.class_, BelongsToOrgMixin | OrgBase)
        for mapper in orm_execute_state.all_mappers
    ):
        # operation has nothing to do with models owned by org
        return
    if orm_execute_state.is_select:
        requester = corvic.context.requester.get()
        org_id = OrgID(requester.org_id)
        if org_id.is_super_user:
            return

        if org_id.is_nobody:
            raise RequestedObjectsForNobodyError(
                "requester org from context was nobody"
            )
        orm_id = org_id.to_orm().unwrap_or_raise()

        # this goofy syntax doesn't typecheck well, but is the documented way to apply
        # these operations to all subclasses (recursive). Sqlalchemy is inspecting the
        # lambda rather than just executing it so a function won't work.
        # https://docs.sqlalchemy.org/en/20/orm/queryguide/api.html#sqlalchemy.orm.with_loader_criteria
        check_org_id_lambda: Callable[  # noqa: E731
            [type[BelongsToOrgMixin]], sa.ColumnElement[bool]
        ] = lambda cls: cls.org_id == orm_id
        orm_execute_state.statement = orm_execute_state.statement.options(
            sa_orm.with_loader_criteria(
                BelongsToOrgMixin,
                cast(Any, check_org_id_lambda),
                include_aliases=True,
                track_closure_variables=False,
            ),
            sa_orm.with_loader_criteria(
                OrgBase,
                OrgBase.id == orm_id,
                include_aliases=True,
                track_closure_variables=False,
            ),
        )


class BadUpdateError(DeletedObjectError):
    """Raised on illegal updates to deleted objects."""

    def __init__(self):
        super().__init__(message="updating deleted object")


class BadDeleteError(DeletedObjectError):
    """Raised when deleting deleted objects."""

    def __init__(self):
        super().__init__(message="deleting an object that is already deleted")


def _report_modifications_to_soft_delete_objects(
    session: sa_orm.Session, flush_context: UOWTransaction, instances: None | Any
):
    for obj in filter(session.is_modified, session.dirty):
        if isinstance(obj, SoftDeleteMixin):
            obj.assert_update_is_allowed()


def _filter_deleted_objects_when_orm_loading(
    execute_state: sa_orm.session.ORMExecuteState,
):
    # check if the orm operation was submitted with an option to force load despite
    # soft-load status and if so just skip this event
    if any(
        isinstance(opt, SoftDeleteMixin.ForceLoadOption)
        for opt in execute_state.user_defined_options
    ) or any(
        isinstance(opt, SoftDeleteMixin.ForceLoadOption)
        for opt in execute_state.local_execution_options.values()
    ):
        return

    def where_criteria(cls: type[SoftDeleteMixin]) -> sa.ColumnElement[bool]:
        return ~cls.is_deleted

    execute_state.statement = execute_state.statement.options(
        sa_orm.with_loader_criteria(
            entity_or_base=SoftDeleteMixin,
            # suppressing pyright is unfortunately required as there seems to be a
            # problem with sqlalchemy.orm.util::LoaderCriteriaOption which will
            # construct a 'DeferredLambdaElement' when `where_criteria` is callable.
            # However, the type annotations are not consistent with the implementation.
            # The implementation, on callables criteria, passes to the lambda the
            # mapping class for using in constructing the `ColumnElement[bool]` result
            # needed. For this reason we ignore the argument type.
            where_criteria=where_criteria,
            include_aliases=True,
        )
    )


class SoftDeleteMixin(sa_orm.MappedAsDataclass):
    """Mixin to make corvic orm models use soft-delete.

    Modifications to objects which are marked as deleted will result in
    an error.
    """

    class ForceLoadOption(sa_orm.UserDefinedOption):
        """Option for ignoring soft delete status when loading."""

    deleted_at: sa_orm.Mapped[datetime | None] = sa_orm.mapped_column(
        sa.DateTime,
        server_default=None,
        nullable=True,
        default=None,
    )
    _frozen = False

    @classmethod
    def _force_load_option(cls):
        return cls.ForceLoadOption()

    @classmethod
    def force_load_options(cls):
        """Options to force load soft-deleted objects when using session.get."""
        return [cls._force_load_option()]

    @classmethod
    def force_load_execution_options(cls):
        """Options to force load soft-deleted objects when using session.execute.

        Also works with session.scalars.
        """
        return {"ignored_option_name": cls._force_load_option()}

    def mark_deleted(self):
        """Updates soft-delete object.

        Note: users should not use this directly and instead should use
        `session.delete(obj)`.
        """
        if self.deleted_at is not None:
            raise BadDeleteError()
        self.deleted_at = datetime.now(tz=timezone.utc)

    @sa_orm.reconstructor  # pyright: ignore[reportUnknownMemberType]
    def _set_frozen_state(self):
        if self.deleted_at is not None:
            self._frozen = True

    @property
    def is_frozen(self):
        return self._frozen

    @hybrid_property
    def is_deleted(self):  # pyright: ignore[reportRedeclaration]
        """Useful when constructing queries for direct use (e.g via `session.execute`).

        ORM users can rely on the typical session interfaces for checking object
        persistence.
        """
        return self.deleted_at is not None

    @is_deleted.expression
    @classmethod
    def is_deleted(cls):
        return cls.deleted_at.is_not(None)

    def assert_update_is_allowed(self):
        """Raises error when called for objects frozen (due to deletion)."""
        if not self.is_frozen:
            return
        raise BadUpdateError()

    @staticmethod
    def register_session_event_listeners(session: type[sa_orm.Session]):
        event.listen(
            session, "before_flush", _report_modifications_to_soft_delete_objects
        )
        event.listen(
            session, "do_orm_execute", _filter_deleted_objects_when_orm_loading
        )


class BelongsToOrgMixin(sa_orm.MappedAsDataclass):
    """Mark models that should be subject to org level access control."""

    @staticmethod
    def _current_org_id_from_context():
        requester = corvic.context.requester.get()
        return OrgID(requester.org_id)

    @staticmethod
    def _make_org_id_default() -> str | None:
        org_id = BelongsToOrgMixin._current_org_id_from_context()

        if org_id.is_nobody:
            raise RequestedObjectsForNobodyError(
                "the nobody org cannot change orm objects"
            )

        if org_id.is_super_user:
            return None

        return org_id.to_orm().unwrap_or_raise()

    org_id: sa_orm.Mapped[str | None] = sa_orm.mapped_column(
        OrgBase.foreign_key().make(ondelete="CASCADE"),
        nullable=False,
        default_factory=_make_org_id_default,
        init=False,
    )

    @sa_orm.validates("org_id")
    def validate_org_id(self, _key: str, orm_id: str | None):
        expected_org_id = self._current_org_id_from_context()
        if expected_org_id.is_nobody:
            raise RequestedObjectsForNobodyError(
                "the nobody org cannot change orm objects"
            )

        if expected_org_id.is_super_user:
            return orm_id

        if orm_id != expected_org_id.to_orm().unwrap_or_raise():
            raise BadArgumentError("provided org_id must match the current org")

        return orm_id

    @staticmethod
    def register_session_event_listeners(session: type[sa_orm.Session]):
        event.listen(session, "do_orm_execute", _filter_org_objects)


class Session(sa_orm.Session):
    """Wrapper around sqlalchemy.orm.Session."""

    _soft_deleted: dict[sa_orm.InstanceState[Any], Any] | None = None

    def _track_soft_deleted(self, instance: object):
        if self._soft_deleted is None:
            self._soft_deleted = {}
        self._soft_deleted[sa_orm.attributes.instance_state(instance)] = instance

    def _reset_soft_deleted(self):
        self._soft_deleted = {}

    def _ensure_persistence(self, instance: object):
        instance_state = sa_orm.attributes.instance_state(instance)
        if instance_state.key is None:
            raise exc.InvalidRequestError("Instance is not persisted")

    def _delete_soft_deleted(self, instance: SoftDeleteMixin):
        self._ensure_persistence(instance)

        instance.mark_deleted()

        # Soft deleted should be tracked so that way a deleted soft-delete instance is
        # correctly identified as being "deleted"
        self._track_soft_deleted(instance)

        # Flushing the objects being deleted is needed to ensure the 'soft-delete'
        # impact is spread. This is because sqlalchemy flush implementation is doing
        # the heavy lifting of updating deleted/modified state across dependencies
        # after flushing. Ensuring this is done necessary to ensure relationships with
        # cascades have valid state after a soft-delete. Otherwise divergence between
        # hard-delete and soft-delete will be seen here (and surprise the user).
        # Note: the cost is reduced by limiting the flush to the soft-delete instance.
        self.flush([instance])

        # Invalidate existing session references for expected get-after-delete behavior.
        if sa_orm.attributes.instance_state(instance).session_id is self.hash_key:
            self.expunge(instance)

    def commit(self):
        super().commit()
        if self._soft_deleted:
            self._reset_soft_deleted()

    def rollback(self):
        super().rollback()
        if self._soft_deleted:
            for obj in self._soft_deleted.values():
                if isinstance(obj, SoftDeleteMixin):
                    obj.deleted_at = None
                    continue
                raise RuntimeError("non-soft delete object in soft deleted set")
            self._reset_soft_deleted()

    @property
    def deleted(self):
        deleted = super().deleted
        if self._soft_deleted:
            deleted.update(self._soft_deleted.values())
        return deleted

    def delete(self, instance: object, *, force_hard_delete=False):
        if isinstance(instance, SoftDeleteMixin) and not force_hard_delete:
            self._delete_soft_deleted(instance)
            return
        super().delete(instance)


SoftDeleteMixin.register_session_event_listeners(Session)
BelongsToOrgMixin.register_session_event_listeners(Session)
