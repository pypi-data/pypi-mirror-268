import json
from typing import Any, NamedTuple


class Schema(NamedTuple):
    all_fields: dict
    default_fields: dict
    discrete: bool
    no_default: bool
    no_null: bool

    def __call__(
        self,
        __discrete__: bool = None,  # type: ignore
        __no_default__: bool = None,  # type: ignore
        __no_null__: bool = None,  # type: ignore
        **kwargs,
    ) -> dict:
        """
        :__discrete__: When `true`, excludes fields with a `null` default value. Explicitly setting the value to `null` will include it.

        :__no_default__: When `true`, default values are excluded.

        :__no_null__: When `true`, `null` values will never be included.
        """
        if __discrete__ == None:
            __discrete__ = self.discrete

        if __no_default__ == None:
            __no_default__ = self.no_default

        if __no_null__ == None:
            __no_null__ = self.no_null

        result = {}

        if not __no_default__:
            for key in self.default_fields:
                value = self.default_fields[key]

                if (__discrete__ or __no_null__) and value == None:
                    continue

                if callable(value):
                    result[key] = value()
                else:
                    result[key] = value

        for key in kwargs:
            if key.startswith("__") and key.endswith("__"):
                continue

            if key in self.default_fields:
                if not __no_null__ or kwargs[key] != None:
                    result[key] = kwargs[key]
            else:
                raise Exception(f"Key '{key}' does not exist!")

        return result

    @staticmethod
    def new(
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
        return schema(
            *json_paths,
            __discrete__=__discrete__,
            __no_default__=__no_default__,
            __no_null__=__no_null__,
            **fields,
        )


def schema(
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
    # Get all fields.

    all_fields: dict[str, Any] = {}

    for path in json_paths:
        with open(path, "r") as f:
            json_fields = json.loads(f.read())

            for key in json_fields:
                all_fields[key] = json_fields[key]

    for key in fields:
        all_fields[key] = fields[key]

    # Get default fields.

    default_fields: dict[str, Any] = {}

    for key in all_fields:
        if key.startswith("__") and key.endswith("__"):
            continue

        default_fields[key] = all_fields[key]

    # Create generator.

    return Schema(
        all_fields=all_fields,
        default_fields=default_fields,
        discrete=__discrete__,
        no_default=__no_default__,
        no_null=__no_null__,
    )
