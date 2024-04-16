from .schema import Schema
from typing import Union


class SchemaPool:
    def __getattr__(self, key: str) -> Schema:
        raise Exception(f"Schema '{key}' does not exist!")

    def __getitem__(self, key: str) -> Schema:
        raise Exception(f"Schema '{key}' does not exist!")

    def set(
        self,
        name: str,
        *args: Union[str, dict],
        __discrete__=False,
        __no_default__=False,
        __no_null__=False,
        **kwargs,
    ):
        """
        :__discrete__: When `true`, excludes fields with a `null` default value. Explicitly setting the value to `null` will include it.

        :__no_default__: When `true`, default values are excluded.

        :__no_null__: When `true`, `null` values will never be included.
        """
        schema = Schema.new(
            *args,
            __discrete__=__discrete__,
            __no_default__=__no_default__,
            __no_null__=__no_null__,
            **kwargs,
        )

        setattr(self, name, schema)

        return schema
