"""Defines a sqlalchemy function for utcnow instead of sqlalchemy.func.now()."""

from typing import Any

from sqlalchemy import sql
from sqlalchemy.ext.compiler import (
    compiles,  # pyright: ignore[reportUnknownVariableType]
)
from sqlalchemy.types import DateTime


class UTCNow(sql.expression.FunctionElement[Any]):
    """Adds a utcnow() expression based on backend db used.

    Implementation follows from documentation from sqlalchemy source at
    sqlalchemy/ext/compiler.py.
    """

    type = DateTime()
    inherit_cache = True


@compiles(UTCNow, "postgresql")
def pg_utcnow(
    element: sql.expression.FunctionElement[Any],
    compiler: sql.compiler.SQLCompiler,
    **kw: Any,
):
    """Compile utc timestamp for postgres."""
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


@compiles(UTCNow)
def default_sql_utcnow(
    element: sql.expression.FunctionElement[Any],
    compiler: sql.compiler.SQLCompiler,
    **kw: Any,
):
    """Compile utc timestamp for other databases."""
    # this matches sqlalchemy.func.now() and is valid for postgresql
    return "CURRENT_TIMESTAMP"


@compiles(UTCNow, "sqlite")
def sqlite_sql_utcnow(
    element: sql.expression.FunctionElement[Any],
    compiler: sql.compiler.SQLCompiler,
    **kw: Any,
):
    """Compile utc timestamp for sqlite."""
    # default now() visitor for sqlite simply returns 'CURRENT_TIMESTAMP'
    # instead we can use STRFTIME with utcnow format
    return r"(STRFTIME('%Y-%m-%d %H:%M:%f', 'NOW'))"
