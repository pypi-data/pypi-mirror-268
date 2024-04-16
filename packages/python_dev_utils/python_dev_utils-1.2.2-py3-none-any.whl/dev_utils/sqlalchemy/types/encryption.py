from typing import TYPE_CHECKING, Any

from sqlalchemy import String, Text, TypeDecorator, func, type_coerce

if TYPE_CHECKING:
    from sqlalchemy.engine import Dialect


class PGPString(TypeDecorator[str]):
    impl = String

    cache_ok = True

    def __init__(self, passphrase: str) -> None:
        super().__init__()
        self.passphrase = passphrase

    @property
    def python_type(self) -> type[str]:  # noqa: D102  # pragma: no coverage
        return str

    def load_dialect_impl(self, dialect: "Dialect") -> Any:
        if dialect.name in {"mysql", "mariadb"}:
            return dialect.type_descriptor(Text())
        if dialect.name == "oracle":
            return dialect.type_descriptor(String(length=4000))
        return dialect.type_descriptor(String())

    def process_bind_param(self, value: Any, dialect: "Dialect") -> str | None:
        if value is None:
            return value
        if not isinstance(value, str):  # pragma: nocover
            value = repr(value)
        value = value.encode()
        return func.pgp_sym_encrypt(value, self.passphrase)  # type: ignore[return-value]

    def process_result_value(self, value: Any, dialect: Dialect) -> str | None:
        if value is None:
            return value
        if not isinstance(value, str):  # pragma: nocover
            value = str(value)
        return func.pgp_sym_decrypt(value, self.passphrase)  # type: ignore[return-value]
