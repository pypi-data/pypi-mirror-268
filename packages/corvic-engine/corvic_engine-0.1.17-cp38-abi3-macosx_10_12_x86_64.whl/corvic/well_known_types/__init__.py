"""Type aliases used across corvic."""

import os
from collections.abc import Iterable, Mapping
from typing import Any, TypeAlias

PathLike: TypeAlias = str | bytes | os.PathLike[Any]

JSONExpressable = (
    bool
    | int
    | str
    | float
    | None
    | Iterable["JSONExpressable"]
    | Mapping[str, "JSONExpressable"]
)

__all__ = [
    "JSONExpressable",
    "PathLike",
]
