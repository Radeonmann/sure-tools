from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.reset_initiated_response import ResetInitiatedResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/api/v1/users/reset",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ResetInitiatedResponse | None:
    if response.status_code == 200:
        response_200 = ResetInitiatedResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ResetInitiatedResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | ResetInitiatedResponse]:
    """Reset account

     Resets all financial data (accounts, categories, merchants, tags, etc.) for the current user's
    family while keeping the user account intact. The reset runs asynchronously in the background. The
    returned job_id is informational only; reset status is family-scoped, not job-scoped. Requires admin
    role.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ResetInitiatedResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | ResetInitiatedResponse | None:
    """Reset account

     Resets all financial data (accounts, categories, merchants, tags, etc.) for the current user's
    family while keeping the user account intact. The reset runs asynchronously in the background. The
    returned job_id is informational only; reset status is family-scoped, not job-scoped. Requires admin
    role.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ResetInitiatedResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | ResetInitiatedResponse]:
    """Reset account

     Resets all financial data (accounts, categories, merchants, tags, etc.) for the current user's
    family while keeping the user account intact. The reset runs asynchronously in the background. The
    returned job_id is informational only; reset status is family-scoped, not job-scoped. Requires admin
    role.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ResetInitiatedResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | ResetInitiatedResponse | None:
    """Reset account

     Resets all financial data (accounts, categories, merchants, tags, etc.) for the current user's
    family while keeping the user account intact. The reset runs asynchronously in the background. The
    returned job_id is informational only; reset status is family-scoped, not job-scoped. Requires admin
    role.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ResetInitiatedResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
