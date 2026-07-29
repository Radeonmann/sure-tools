from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.post_api_v1_auth_sso_create_account_body import PostApiV1AuthSsoCreateAccountBody
from ...models.post_api_v1_auth_sso_create_account_response_200 import PostApiV1AuthSsoCreateAccountResponse200
from ...models.post_api_v1_auth_sso_create_account_response_422 import PostApiV1AuthSsoCreateAccountResponse422
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiV1AuthSsoCreateAccountBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/auth/sso_create_account",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PostApiV1AuthSsoCreateAccountResponse200 | PostApiV1AuthSsoCreateAccountResponse422 | None:
    if response.status_code == 200:
        response_200 = PostApiV1AuthSsoCreateAccountResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = PostApiV1AuthSsoCreateAccountResponse422.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | PostApiV1AuthSsoCreateAccountResponse200 | PostApiV1AuthSsoCreateAccountResponse422]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostApiV1AuthSsoCreateAccountBody,
) -> Response[ErrorResponse | PostApiV1AuthSsoCreateAccountResponse200 | PostApiV1AuthSsoCreateAccountResponse422]:
    """Create a new account via SSO

     Creates a new user and family from a previously issued linking code. Links the SSO identity via
    OidcIdentity, logs the JIT account creation via SsoAuditLog, and issues mobile OAuth tokens. The
    linking code must have allow_account_creation enabled.

    Args:
        body (PostApiV1AuthSsoCreateAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostApiV1AuthSsoCreateAccountResponse200 | PostApiV1AuthSsoCreateAccountResponse422]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    body: PostApiV1AuthSsoCreateAccountBody,
) -> ErrorResponse | PostApiV1AuthSsoCreateAccountResponse200 | PostApiV1AuthSsoCreateAccountResponse422 | None:
    """Create a new account via SSO

     Creates a new user and family from a previously issued linking code. Links the SSO identity via
    OidcIdentity, logs the JIT account creation via SsoAuditLog, and issues mobile OAuth tokens. The
    linking code must have allow_account_creation enabled.

    Args:
        body (PostApiV1AuthSsoCreateAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostApiV1AuthSsoCreateAccountResponse200 | PostApiV1AuthSsoCreateAccountResponse422
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostApiV1AuthSsoCreateAccountBody,
) -> Response[ErrorResponse | PostApiV1AuthSsoCreateAccountResponse200 | PostApiV1AuthSsoCreateAccountResponse422]:
    """Create a new account via SSO

     Creates a new user and family from a previously issued linking code. Links the SSO identity via
    OidcIdentity, logs the JIT account creation via SsoAuditLog, and issues mobile OAuth tokens. The
    linking code must have allow_account_creation enabled.

    Args:
        body (PostApiV1AuthSsoCreateAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostApiV1AuthSsoCreateAccountResponse200 | PostApiV1AuthSsoCreateAccountResponse422]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostApiV1AuthSsoCreateAccountBody,
) -> ErrorResponse | PostApiV1AuthSsoCreateAccountResponse200 | PostApiV1AuthSsoCreateAccountResponse422 | None:
    """Create a new account via SSO

     Creates a new user and family from a previously issued linking code. Links the SSO identity via
    OidcIdentity, logs the JIT account creation via SsoAuditLog, and issues mobile OAuth tokens. The
    linking code must have allow_account_creation enabled.

    Args:
        body (PostApiV1AuthSsoCreateAccountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostApiV1AuthSsoCreateAccountResponse200 | PostApiV1AuthSsoCreateAccountResponse422
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
