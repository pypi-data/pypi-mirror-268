import json
from typing import TYPE_CHECKING, Any, TypeVar

from pydantic.version import version_short
from sqlalchemy import JSON as JSON_COLUMN
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.types import JSON as JSON_TYPE
from sqlalchemy.types import TypeDecorator

if TYPE_CHECKING:
    from sqlalchemy import Dialect

pydantic_version = tuple(map(int, version_short().split(".")))
T = TypeVar("T")

is_pydantic_v2 = pydantic_version >= (2, 0)

if is_pydantic_v2:
    from pydantic import TypeAdapter
    from pydantic_core import to_jsonable_python as pydantic_encoder

    def _parse_obj_as(type_: type[T], obj: Any) -> T:  # noqa: ANN401
        return TypeAdapter(type_).validate_python(obj)

else:
    from pydantic import parse_obj_as as _parse_obj_as  # type: ignore
    from pydantic.json import pydantic_encoder


def _to_dict(value: Any) -> Any:  # noqa: ANN401
    return json.loads(json.dumps(value, default=pydantic_encoder))


def json_serializer(obj: Any, **kwargs: Any) -> str:  # noqa: ANN401
    """Serialize obj to json str with pydantic_encoder option."""
    return json.dumps(obj, default=pydantic_encoder, **kwargs)


class PydanticType(TypeDecorator[T]):
    """Type decorator for JSON field as pydantic model."""

    impl = JSON_TYPE

    def __init__(self, pydantic_type: type[T]) -> None:
        super().__init__()
        self.pydantic_type = pydantic_type

    def load_dialect_impl(self, dialect: "Dialect"):  # noqa: D102, ANN201
        if dialect.name == "postgresql":
            return dialect.type_descriptor(JSONB())
        else:
            return dialect.type_descriptor(JSON_COLUMN())

    def process_bind_param(  # noqa: D102
        self,
        value: "T | None",
        dialect: "Dialect",  # noqa
    ) -> "T | None":
        return _to_dict(value) if value else None

    def process_result_value(  # noqa: D102
        self,
        value: "T | None",
        dialect: "Dialect",  # noqa
    ) -> "T | None":
        return _parse_obj_as(self.pydantic_type, value) if value else None
