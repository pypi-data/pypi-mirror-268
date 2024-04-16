"""Rockset sqlglot Dialect and helpers."""

from sqlglot import exp, generator, tokens, transpile
from sqlglot.dialects.dialect import Dialect as GlotDialect


def collection(workspace: str, collection: str) -> exp.Table:
    return exp.Table(
        this=exp.Identifier(this=collection, quoted=True),
        db=exp.Identifier(this=workspace, quoted=True),
    )


class Dialect(GlotDialect):
    """SQL Dialect for Rockset."""

    class Tokenizer(tokens.Tokenizer):
        """Tokenizer configuration for Rockset SQL Dialect."""

        # We cannot add ClassVar here to avoid noqa RUF012 as these are
        # assignments (to base class members) not definitions (of new class
        # members)

        QUOTES = ["'", '"']  # noqa: RUF012
        IDENTIFIERS = ['"']  # noqa: RUF012

        KEYWORDS = {  # noqa: RUF012
            **tokens.Tokenizer.KEYWORDS,
            "INT64": tokens.TokenType.BIGINT,
            "FLOAT64": tokens.TokenType.DOUBLE,
        }

    class Generator(generator.Generator):
        """Generator configuration for Rockset SQL Dialect."""

        def _transform_array_expression(self, expression: exp.Expression | None):
            return f"[{self.expressions(expression)}]"

        def _transform_struct_expression(self, expression: exp.Expression | None):
            return f"{{{self.expressions(expression)}}}"

        TRANSFORMS = {  # noqa: RUF012
            exp.Array: _transform_array_expression,
            exp.Struct: _transform_struct_expression,
        }

        # following documentation from rockset: https://rockset.com/docs/data-types/
        TYPE_MAPPING = {  # noqa: RUF012
            # string types are all equivalent string == varchar == text == char
            exp.DataType.Type.TEXT: "string",
            exp.DataType.Type.VARCHAR: "varchar",
            exp.DataType.Type.CHAR: "char",
            # TODO(yasser): rockset also has "undefined"
            exp.DataType.Type.NULL: "null",
            exp.DataType.Type.TINYINT: "int",
            exp.DataType.Type.SMALLINT: "int",
            exp.DataType.Type.INT: "integer",
            exp.DataType.Type.BIGINT: "int64",
            exp.DataType.Type.FLOAT: "float",
            exp.DataType.Type.DOUBLE: "double",
            exp.DataType.Type.BOOLEAN: "bool",
            exp.DataType.Type.BINARY: "bytes",
            exp.DataType.Type.INT256: "u256",
            exp.DataType.Type.OBJECT: "object",
            exp.DataType.Type.DATE: "date",
            exp.DataType.Type.DATETIME: "datetime",
            exp.DataType.Type.TIME: "time",
            exp.DataType.Type.TIMESTAMP: "timestamp",
            exp.DataType.Type.ARRAY: "array",
        }


def format_query(sql: str) -> str:
    """Formats SQL query raising a ParseError if the statement cannot be parsed."""
    return transpile(sql=sql, read=Dialect, write=Dialect, pretty=True)[0]
