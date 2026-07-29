from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.retry_response import RetryResponse
from ...types import Response


def _get_kwargs(
    chat_id: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/chats/{chat_id}/messages/retry".format(
            chat_id=quote(str(chat_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | RetryResponse | None:
    if response.status_code == 202:
        response_202 = RetryResponse.from_dict(response.json())

        return response_202

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | RetryResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    chat_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | RetryResponse]:
    """Retry the last assistant response

    Args:
        chat_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | RetryResponse]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    chat_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | RetryResponse | None:
    """Retry the last assistant response

    Args:
        chat_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | RetryResponse
    """

    return sync_detailed(
        chat_id=chat_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    chat_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[ErrorResponse | RetryResponse]:
    """Retry the last assistant response

    Args:
        chat_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | RetryResponse]
    """

    kwargs = _get_kwargs(
        chat_id=chat_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    chat_id: str,
    *,
    client: AuthenticatedClient,
) -> ErrorResponse | RetryResponse | None:
    """Retry the last assistant response

    Args:
        chat_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | RetryResponse
    """

    return (
        await asyncio_detailed(
            chat_id=chat_id,
            client=client,
        )
    ).parsed
