from dataclasses import dataclass
from importlib import import_module
from types import ModuleType
from typing import Any, Callable, Coroutine, Optional, Union
from urllib.parse import urlparse
from uuid import UUID

from annotated_types import Ge, Le
from pydantic import AfterValidator, AnyUrl, BaseModel, GetPydanticSchema, SecretStr
from pydantic_core import core_schema
from pydantic_settings import BaseSettings
from typing_extensions import Annotated

from arrlio.settings import TASK_MAX_PRIORITY, TASK_MIN_PRIORITY

AsyncCallable = Callable[..., Coroutine]
ExceptionFilter = Callable[[Exception], bool]


Timeout = Annotated[int, Ge(0)]

Ttl = Annotated[int, Ge(1)]

TaskPriority = Annotated[int, Ge(TASK_MIN_PRIORITY), Le(TASK_MAX_PRIORITY)]

TaskId = Union[str, UUID]
Args = Union[list, tuple]
Kwds = dict


@dataclass
class ModuleConstraints:
    has_attrs: Optional[list[str]]

    def __hash__(self):
        return hash(";".join(self.has_attrs or []))

    def __call__(self, v):
        if self.has_attrs:
            for name in self.has_attrs:
                if not hasattr(v, name):
                    raise ValueError(f"module doesn't provide required attribute '{name}'")
        return v


class Module(ModuleType):
    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler):  # pylint: disable=unused-argument
        def validate_from_str(v):
            if isinstance(v, str):
                try:
                    v = import_module(v)
                except ModuleNotFoundError as e:
                    raise ValueError("module not found") from e
            return v

        from_str_schema = core_schema.chain_schema(
            [
                core_schema.str_schema(),
                core_schema.no_info_plain_validator_function(validate_from_str),
            ]
        )

        return core_schema.union_schema(
            [
                core_schema.is_instance_schema(ModuleType),
                from_str_schema,
            ],
            serialization=core_schema.plain_serializer_function_ser_schema(
                function=lambda x: x.__spec__ and x.__spec__.name or f"{x}",
                when_used="json",
            ),
        )

    # @classmethod
    # def __get_pydantic_json_schema__(cls, core_schema, handler):
    #     return handler(core_schema.str_schema())


BackendModule = Annotated[Module, AfterValidator(ModuleConstraints(has_attrs=["Backend", "Config"]))]

SerializerModule = Annotated[Module, AfterValidator(ModuleConstraints(has_attrs=["Serializer", "Config"]))]

ExecutorModule = Annotated[Module, AfterValidator(ModuleConstraints(has_attrs=["Executor", "Config"]))]

PluginModule = Annotated[Module, AfterValidator(ModuleConstraints(has_attrs=["Plugin", "Config"]))]


ModuleConfig = Annotated[
    Union[BaseModel, BaseSettings],
    GetPydanticSchema(
        lambda source_type, handler: core_schema.no_info_after_validator_function(
            lambda v: v,
            core_schema.is_instance_schema((dict, source_type)),
        )
    ),
    GetPydanticSchema(
        lambda source_type, handler: core_schema.no_info_before_validator_function(
            lambda v: v,
            core_schema.chain_schema([core_schema.is_instance_schema((dict, source_type)), handler(source_type)]),
        )
    ),
]


class SecretAnyUrl(AnyUrl):
    def __new__(cls, url) -> object:
        if hasattr(url, "get_secret_value"):
            url = url.get_secret_value()
        else:
            url = f"{url}"
        original = urlparse(url)
        if original.username or original.password:
            url = original._replace(
                netloc=f"***:***@{original.hostname}" + (f":{original.port}" if original.port is not None else "")
            ).geturl()
        obj = super().__new__(cls, url)
        obj._original_str = str(AnyUrl(original.geturl()))
        obj._username = SecretStr(original.username) if original.username else None
        obj._password = SecretStr(original.password) if original.password else None
        return obj

    @property
    def username(self) -> SecretStr:
        return self._username

    @property
    def password(self) -> SecretStr:
        return self._password

    @classmethod
    def __get_pydantic_core_schema__(cls, source_type: Any, handler):
        return core_schema.no_info_before_validator_function(
            lambda v: v if isinstance(v, cls) else cls(v),
            core_schema.chain_schema([core_schema.is_instance_schema(source_type), handler(source_type)]),
            serialization=core_schema.plain_serializer_function_ser_schema(
                lambda v: v,
                info_arg=False,
                return_schema=core_schema.url_schema(),
            ),
        )

    def __repr__(self) -> str:
        return f"SecretAnyUrl('{self}')"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, SecretAnyUrl) and self.get_secret_value() == other.get_secret_value()

    def __hash__(self):
        return hash(self._original_str)  # pylint: disable=no-member

    def get_secret_value(self) -> str:
        return self._original_str  # pylint: disable=no-member


@dataclass
class UrlConstraints:
    allowed_schemes: Optional[list[str]]

    def __hash__(self):
        return hash(";".join(self.allowed_schemes or []))

    def __call__(self, v):
        if self.allowed_schemes and v.scheme not in self.allowed_schemes:
            raise ValueError(f"url scheme should be one of {self.allowed_schemes}")
        return v


SecretHttpUrl = Annotated[
    SecretAnyUrl,
    AfterValidator(UrlConstraints(allowed_schemes=["http", "https"])),
]


SecretAmqpDsn = Annotated[
    SecretAnyUrl,
    AfterValidator(UrlConstraints(allowed_schemes=["amqp", "amqps"])),
]
