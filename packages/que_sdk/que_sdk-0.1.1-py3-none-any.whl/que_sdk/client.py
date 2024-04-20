import http
from typing import (
    Any,
)

from que_sdk.clients import (
    AuthClient,
    RoleClient,
    UserClient,
)

# noinspection PyProtectedMember
from que_sdk.schemas import (
    LoginSchema,
    ResetPasswordSchema,
    RoleSchema,
    SignUpSchema,
    TMELoginSchema,
    UserSchema,
)
from que_sdk.types import (
    ClientsNameT,
    FlexibleResponseT,
    ResponseT,
)

__all__ = ("Client",)


class Client:
    def __init__(self) -> None:
        self._clients = {
            "auth": AuthClient(),
            "user": UserClient(),
            "role": RoleClient(),
        }

    def get_client(self, client_name: ClientsNameT) -> Any:
        if client_name not in self._clients:
            raise ValueError(f"Unknown client: {client_name}")
        return self._clients[client_name]

    async def signup(self, data_in: SignUpSchema) -> ResponseT[dict[str, Any]]:
        """
        Register a new user.

        :param data_in: SignUpSchema object containing user registration data, including
                        username, telegram_id (optional), and password (optional)
        :return: status code and response dictionary with user data
        """
        client = self.get_client("auth")
        return await client.signup(data_in)

    async def login_t_me(self, data_in: TMELoginSchema) -> ResponseT[dict[str, Any]]:
        """
         Login to the user's telegram account.

        :param data_in: TMELoginSchema object containing TME login data, including
                        telegram_id, signature, nonce, and timestamp
        :return: status code and response dictionary with access and refresh token
        """
        client = self.get_client("auth")
        return await client.login_t_me(data_in)

    async def login(self, data_in: LoginSchema) -> ResponseT[dict[str, Any]]:
        """
        Login to the user's account.

        :param data_in: LoginSchema object containing login data, including
                        username and password
        :return: status code and response dictionary with access token and user data
        """
        client = self.get_client("auth")
        return await client.login(data_in)

    async def reset_password(self, data_in: ResetPasswordSchema) -> ResponseT[str]:
        """
        Reset user password.

        :param data_in: ResetPasswordSchema object containing old password, new password,
                        and repeated new password
        :return: status code and response message
        """
        client = self.get_client("auth")
        return await client.reset_password(data_in)

    async def get_users(self) -> ResponseT[list[dict[str, Any]]]:
        """
        Get a list of all users.

        :return: status code and list of users
        """
        client = self.get_client("user")
        return await client.get_users()

    async def get_user_me(self, access_token: str) -> ResponseT[dict[str, Any]]:
        """
        Get information about the current user.

        :param access_token: access token
        :return: status code and user information
        """
        client = self.get_client("user")
        return await client.get_user_me(access_token)

    async def update_user_me(self, data_in: UserSchema) -> ResponseT[dict[str, Any]]:
        """
        Update information about the current user.

        :param data_in: user data to update
        :return: status code and updated user information
        """
        client = self.get_client("user")
        return await client.update_user_me(data_in)

    async def deactivate_user_me(self, access_token: str) -> http.HTTPStatus:
        """
        Deactivate the current user.

        :param access_token: access token
        :return: status code
        """
        client = self.get_client("user")
        return await client.deactivate_user_me(access_token)

    async def reactivate_user(self, access_token: str) -> http.HTTPStatus:
        """
        Reactivate the current user.

        :param access_token: access token
        :return: status code
        """
        client = self.get_client("user")
        return await client.reactivate_user(access_token)

    async def create_role(
        self,
        data_in: RoleSchema,
        access_token: str,
    ) -> ResponseT[dict[str, Any]]:
        """
        Create a new role.

        :param data_in: RoleSchema object containing role data, including title
        :param access_token: access token for authentication
        :return: status code and response dictionary with role data
        """
        client = self.get_client("role")
        return await client.create_role(data_in, access_token)

    async def get_role_or_roles(
        self,
        role_id: int | None = None,
        title: str | None = None,
    ) -> ResponseT[FlexibleResponseT]:
        """
        Get roles based on role_id or title.

        :param role_id: role ID to filter roles by (optional)
        :param title: role title to filter roles by (optional)
        :return: status code and response, either a list of roles or a single role
        """
        client = self.get_client("role")
        return await client.get_roles(role_id, title)

    async def update_role_by_id(
        self,
        role_id: int,
        new_title: str,
        access_token: str | None = None,
    ) -> ResponseT[dict[str, Any]]:
        """
        Update a role's title by its ID.

        :param role_id: role ID to update
        :param new_title: new title for the role
        :param access_token: access token for authentication (optional)
        :return: status code and response dictionary with updated role data
        """
        client = self.get_client("role")
        return await client.update_role_by_id(
            role_id=role_id, new_title=new_title, access_token=access_token
        )

    async def delete_role_by_id(
        self, role_id: int, access_token: str | None = None
    ) -> http.HTTPStatus:
        """
        Delete a role by its ID.

        :param role_id: role ID to delete
        :param access_token: access token for authentication (optional)
        :return: status code
        """
        client = self.get_client("role")
        return await client.delete_role_by_id(
            role_id=role_id, access_token=access_token
        )
