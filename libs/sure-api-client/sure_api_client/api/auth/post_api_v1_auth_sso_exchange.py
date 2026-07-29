from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.post_api_v1_auth_sso_exchange_body import PostApiV1AuthSsoExchangeBody
from ...models.post_api_v1_auth_sso_exchange_response_200 import PostApiV1AuthSsoExchangeResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiV1AuthSsoExchangeBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/auth/sso_exchange",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | PostApiV1AuthSsoExchangeResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiV1AuthSsoExchangeResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | PostApiV1AuthSsoExchangeResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostApiV1AuthSsoExchangeBody,
) -> Response[ErrorResponse | PostApiV1AuthSsoExchangeResponse200]:
    """Exchange mobile SSO authorization code for tokens

     Exchanges a one-time authorization code (received via deep link after mobile SSO) for OAuth tokens.
    The code is single-use and expires after 5 minutes.

    Args:
        body (PostApiV1AuthSsoExchangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostApiV1AuthSsoExchangeResponse200]
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
    body: PostApiV1AuthSsoExchangeBody,
) -> ErrorResponse | PostApiV1AuthSsoExchangeResponse200 | None:
    """Exchange mobile SSO authorization code for tokens

     Exchanges a one-time authorization code (received via deep link after mobile SSO) for OAuth tokens.
    The code is single-use and expires after 5 minutes.

    Args:
        body (PostApiV1AuthSsoExchangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostApiV1AuthSsoExchangeResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostApiV1AuthSsoExchangeBody,
) -> Response[ErrorResponse | PostApiV1AuthSsoExchangeResponse200]:
    """Exchange mobile SSO authorization code for tokens

     Exchanges a one-time authorization code (received via deep link after mobile SSO) for OAuth tokens.
    The code is single-use and expires after 5 minutes.

    Args:
        body (PostApiV1AuthSsoExchangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | PostApiV1AuthSsoExchangeResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostApiV1AuthSsoExchangeBody,
) -> ErrorResponse | PostApiV1AuthSsoExchangeResponse200 | None:
    """Exchange mobile SSO authorization code for tokens

     Exchanges a one-time authorization code (received via deep link after mobile SSO) for OAuth tokens.
    The code is single-use and expires after 5 minutes.

    Args:
        body (PostApiV1AuthSsoExchangeBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | PostApiV1AuthSsoExchangeResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
