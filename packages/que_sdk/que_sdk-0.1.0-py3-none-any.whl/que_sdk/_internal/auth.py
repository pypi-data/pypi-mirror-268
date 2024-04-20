from collections.abc import (
    Iterable,
)

from httpx import (
    Auth,
    Request,
)


class JWTAuth(Auth):
    def __init__(self, access_token: str):
        self.access_token = access_token

    def auth_flow(self, request: Request) -> Iterable[tuple[str, str]]:
        request.headers["Authorization"] = f"Bearer {self.access_token}"
        yield request
