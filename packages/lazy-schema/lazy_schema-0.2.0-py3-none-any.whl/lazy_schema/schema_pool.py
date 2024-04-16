from .schema import Schema
from typing import Any, Dict


class SchemaPool:
    schemas: Dict[str, Schema]

    def __init__(self):
        self.schemas = {}

    def __getattr__(self, name: str) -> Schema:
        schema = self.schemas.get(name)

        if schema == None:
            raise Exception(f"Schema '{name}' does not exist!")

        return schema

    def __setattr__(self, name: str, value: Schema):
        self.schemas[name] = value

        return value

    def __getitem__(self, key: str) -> Schema:
        schema = self.schemas.get(key)

        if schema == None:
            raise Exception(f"Schema '{key}' does not exist!")

        return schema

    def __setitem__(self, key: str, value: Schema):
        self.schemas[key] = value

        return value

    def new(
        self,
        name: str,
        *json_paths: str,
        __discrete__=False,
        __no_default__=False,
        __no_null__=False,
        **fields,
    ):
        """
        :__discrete__: When `true`, excludes fields with a `null` default value. Explicitly setting the value to `null` will include it.

        :__no_default__: When `true`, default values are excluded.

        :__no_null__: When `true`, `null` values will never be included.
        """
        schema = Schema.new(
            *json_paths,
            __discrete__=__discrete__,
            __no_default__=__no_default__,
            __no_null__=__no_null__,
            **fields,
        )
        self.schemas[name] = schema

        return schema
