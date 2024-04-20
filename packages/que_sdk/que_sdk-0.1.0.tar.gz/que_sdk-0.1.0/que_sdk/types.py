import http
from typing import (
    Any,
    Literal,
    TypeAlias,
    TypeVar,
)

T = TypeVar("T")

DefaultResponseT: TypeAlias = dict[str, Any]
FlexibleResponseT: TypeAlias = list[DefaultResponseT] | DefaultResponseT
ResponseT: TypeAlias = tuple[http.HTTPStatus, T]
ClientsNameT: TypeAlias = Literal["auth", "user", "role"]
