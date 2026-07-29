from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_detail import AccountDetail
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: UUID,
    *,
    include_disabled: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_disabled"] = include_disabled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/accounts/{id}".format(
            id=quote(str(id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AccountDetail | ErrorResponse | None:
    if response.status_code == 200:
        response_200 = AccountDetail.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AccountDetail | ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    include_disabled: bool | Unset = UNSET,
) -> Response[AccountDetail | ErrorResponse]:
    """Retrieve an account

    Args:
        id (UUID):
        include_disabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountDetail | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        include_disabled=include_disabled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: UUID,
    *,
    client: AuthenticatedClient,
    include_disabled: bool | Unset = UNSET,
) -> AccountDetail | ErrorResponse | None:
    """Retrieve an account

    Args:
        id (UUID):
        include_disabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountDetail | ErrorResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        include_disabled=include_disabled,
    ).parsed


async def asyncio_detailed(
    id: UUID,
    *,
    client: AuthenticatedClient,
    include_disabled: bool | Unset = UNSET,
) -> Response[AccountDetail | ErrorResponse]:
    """Retrieve an account

    Args:
        id (UUID):
        include_disabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountDetail | ErrorResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        include_disabled=include_disabled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: UUID,
    *,
    client: AuthenticatedClient,
    include_disabled: bool | Unset = UNSET,
) -> AccountDetail | ErrorResponse | None:
    """Retrieve an account

    Args:
        id (UUID):
        include_disabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountDetail | ErrorResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            include_disabled=include_disabled,
        )
    ).parsed
