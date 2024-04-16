from __future__ import annotations

import logging
from dataclasses import dataclass
from enum import Enum, IntEnum
from typing import Any, Callable, TypeVar, Type, Union, Dict, Generic, TypedDict, Tuple

from pydantic import BaseModel, Field
from builtins import Exception

from pydantic.fields import FieldInfo

TException = TypeVar("TException", bound=Exception)
TErrorResponse = TypeVar("TErrorResponse", bound=BaseModel)


class LogLevel(IntEnum):
    ignore = -1
    debug = logging.DEBUG  # 10
    info = logging.INFO  # 20
    warning = logging.WARNING  # 30
    error = logging.ERROR  # 40
    critical = logging.CRITICAL  # 50


class ProblemExtension(TypedDict):
    typing: Tuple[Type, FieldInfo]
    parser: Callable[[Any], Any]


@dataclass(slots=True, kw_only=True)
class KnownProblem(Generic[TException]):
    status_code: int
    responsibility: str
    code: str
    log_level: LogLevel
    exception_class: Union[Type[TException], None]
    message: str = ""
    docs: str = ""
    generate_details: Callable[[TException], str] = Field(default=lambda _: "")
    extension: Dict[str, ProblemExtension] = Field(default_factory=dict)


class KnownProblemResponse(BaseModel):
    type: str
    title: str
    status: int
    detail: str
    instance: str
