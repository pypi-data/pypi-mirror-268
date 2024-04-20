import http
from typing import (
    Any,
)

# noinspection PyProtectedMember
from que_sdk._internal import (
    BaseClient,
)
from que_sdk.schemas import (
    LoginSchema,
    ResetPasswordSchema,
    RoleSchema,
    SignUpSchema,
    TMELoginSchema,
    UserSchema,
)
from que_sdk.types import (
    FlexibleResponseT,
    ResponseT,
)

__all__ = ("UserClient", "AuthClient", "RoleClient")


class UserClient(BaseClient):
    async def get_users(self) -> ResponseT[list[dict[str, Any]]]:
        url = f"{self._base_url}/users/"
        status_code, response = await self._make_request(
            method="GET",
            url=url,
        )
        return http.HTTPStatus(status_code), response

    async def get_user_me(self, access_token: str) -> ResponseT[dict[str, Any]]:
        url = f"{self._base_url}/users/me/"
        status_code, response = await self._make_request(
            method="GET",
            url=url,
            access_token=access_token,
        )
        return http.HTTPStatus(status_code), response

    async def update_user_me(self, data_in: UserSchema) -> ResponseT[dict[str, Any]]:
        url = f"{self._base_url}/users/me/"
        status_code, response = await self._make_request(
            method="PATCH",
            url=url,
            data=data_in.model_dump(exclude_none=True),
        )
        return http.HTTPStatus(status_code), response

    async def deactivate_user_me(self, access_token: str) -> http.HTTPStatus:
        """
        Deactivate the current user.

        :param access_token: access token
        :return: status code
        """
        url = f"{self._base_url}/users/me/"
        status_code, _ = await self._make_request(
            method="DELETE",
            url=url,
            access_token=access_token,
        )
        return http.HTTPStatus(status_code)

    async def reactivate_user(self, access_token: str) -> http.HTTPStatus:
        """
        Reactivate the current user.

        :param access_token: access token
        :return: status code
        """
        url = f"{self._base_url}/users/me/"
        status_code, _ = await self._make_request(
            method="POST",
            url=url,
            access_token=access_token,
        )
        return http.HTTPStatus(status_code)


class AuthClient(BaseClient):
    """
    Client for handling user authentication.
    """

    async def signup(self, data_in: SignUpSchema) -> ResponseT[dict[str, Any]]:
        url = f"{self._base_url}/auth/signup/"
        status_code, response = await self._make_request(
            method="POST",
            url=url,
            json=data_in.model_dump(),
        )
        return http.HTTPStatus(status_code), response

    async def login_t_me(self, data_in: TMELoginSchema) -> ResponseT[dict[str, Any]]:
        url = f"{self._base_url}/auth/login/t/me/"
        status_code, response = await self._make_request(
            method="POST",
            url=url,
            json=data_in.model_dump(),
        )
        return http.HTTPStatus(status_code), response

    async def login(self, data_in: LoginSchema) -> ResponseT[dict[str, Any]]:
        url = f"{self._base_url}/auth/login/"
        status_code, response = await self._make_request(
            method="POST",
            url=url,
            json=data_in.model_dump(),
        )
        return http.HTTPStatus(status_code), response

    async def reset_password(self, data_in: ResetPasswordSchema) -> ResponseT[str]:
        url = f"{self._base_url}/auth/reset_password/"
        status_code, response = await self._make_request(
            method="POST",
            url=url,
            json=data_in.model_dump(),
        )
        return http.HTTPStatus(status_code), response


class RoleClient(BaseClient):
    async def crate_role(
        self, data_in: RoleSchema, access_token: str
    ) -> ResponseT[dict[str, Any]]:
        url = f"{self._base_url}/roles/"
        status_code, response = await self._make_request(
            method="POST",
            url=url,
            json=data_in.model_dump(),
            access_token=access_token,
        )
        return http.HTTPStatus(status_code), response

    async def get_roles(
        self,
        role_id: int | None = None,
        title: str | None = None,
    ) -> ResponseT[FlexibleResponseT]:
        params: dict[str, Any] = {}
        if role_id:
            params["role_id"] = role_id
        if title:
            params["title"] = title
        url = f"{self._base_url}/roles/single/"
        status_code, response = await self._make_request(
            method="GET",
            url=url,
            params=params,
        )
        return http.HTTPStatus(status_code), response

    async def update_role_by_id(
        self,
        role_id: int,
        new_title: str,
        access_token: str | None = None,
    ) -> ResponseT[dict[str, Any]]:
        url = f"{self._base_url}/roles/{role_id}/"
        status_code, response = await self._make_request(
            method="PATCH",
            url=url,
            json={"title": new_title},
            access_token=access_token,
        )
        return http.HTTPStatus(status_code), response

    async def delete_role_by_id(
        self, role_id: int, access_token: str | None = None
    ) -> http.HTTPStatus:
        url = f"{self._base_url}/roles/{role_id}/"
        status_code, _ = await self._make_request(
            method="DELETE",
            url=url,
            access_token=access_token,
        )
        return http.HTTPStatus(status_code)
