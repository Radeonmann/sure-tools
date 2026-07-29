from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.mfa_required_response import MfaRequiredResponse
from ...models.post_api_v1_auth_sso_link_body import PostApiV1AuthSsoLinkBody
from ...models.post_api_v1_auth_sso_link_response_200 import PostApiV1AuthSsoLinkResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: PostApiV1AuthSsoLinkBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/auth/sso_link",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ErrorResponse | MfaRequiredResponse | PostApiV1AuthSsoLinkResponse200 | None:
    if response.status_code == 200:
        response_200 = PostApiV1AuthSsoLinkResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:

        def _parse_response_401(data: object) -> ErrorResponse | MfaRequiredResponse:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_401_type_0 = ErrorResponse.from_dict(data)

                return response_401_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_401_type_1 = MfaRequiredResponse.from_dict(data)

            return response_401_type_1

        response_401 = _parse_response_401(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ErrorResponse | MfaRequiredResponse | PostApiV1AuthSsoLinkResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostApiV1AuthSsoLinkBody,
) -> Response[ErrorResponse | ErrorResponse | MfaRequiredResponse | PostApiV1AuthSsoLinkResponse200]:
    """Link an existing account via SSO

     Authenticates with email/password and links the SSO identity from a previously issued linking code.
    Creates an OidcIdentity, logs the link via SsoAuditLog, and issues mobile OAuth tokens.

    Args:
        body (PostApiV1AuthSsoLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ErrorResponse | MfaRequiredResponse | PostApiV1AuthSsoLinkResponse200]
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
    body: PostApiV1AuthSsoLinkBody,
) -> ErrorResponse | ErrorResponse | MfaRequiredResponse | PostApiV1AuthSsoLinkResponse200 | None:
    """Link an existing account via SSO

     Authenticates with email/password and links the SSO identity from a previously issued linking code.
    Creates an OidcIdentity, logs the link via SsoAuditLog, and issues mobile OAuth tokens.

    Args:
        body (PostApiV1AuthSsoLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ErrorResponse | MfaRequiredResponse | PostApiV1AuthSsoLinkResponse200
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    body: PostApiV1AuthSsoLinkBody,
) -> Response[ErrorResponse | ErrorResponse | MfaRequiredResponse | PostApiV1AuthSsoLinkResponse200]:
    """Link an existing account via SSO

     Authenticates with email/password and links the SSO identity from a previously issued linking code.
    Creates an OidcIdentity, logs the link via SsoAuditLog, and issues mobile OAuth tokens.

    Args:
        body (PostApiV1AuthSsoLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ErrorResponse | MfaRequiredResponse | PostApiV1AuthSsoLinkResponse200]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    body: PostApiV1AuthSsoLinkBody,
) -> ErrorResponse | ErrorResponse | MfaRequiredResponse | PostApiV1AuthSsoLinkResponse200 | None:
    """Link an existing account via SSO

     Authenticates with email/password and links the SSO identity from a previously issued linking code.
    Creates an OidcIdentity, logs the link via SsoAuditLog, and issues mobile OAuth tokens.

    Args:
        body (PostApiV1AuthSsoLinkBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ErrorResponse | MfaRequiredResponse | PostApiV1AuthSsoLinkResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
