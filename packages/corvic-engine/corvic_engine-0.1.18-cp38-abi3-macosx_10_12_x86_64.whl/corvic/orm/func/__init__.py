"""Corvic sqlalchemy functions."""

from corvic.orm.func.utc_func import UTCNow as _UTCNow
from corvic.orm.func.uuid_func import UUIDFunction as _UUIDFunction


def utc_now():
    """Sqlalchemy function returning utc now."""
    return _UTCNow()


def gen_uuid():
    """Sqlalchemy function returning a random uuid."""
    return _UUIDFunction()


__all__ = ["utc_now", "gen_uuid"]
