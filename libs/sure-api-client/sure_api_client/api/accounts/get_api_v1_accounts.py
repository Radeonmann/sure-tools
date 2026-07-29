from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_collection import AccountCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    include_disabled: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["include_disabled"] = include_disabled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/accounts",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AccountCollection | None:
    if response.status_code == 200:
        response_200 = AccountCollection.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AccountCollection]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    include_disabled: bool | Unset = UNSET,
) -> Response[AccountCollection]:
    """List accounts

    Args:
        page (int | Unset):
        per_page (int | Unset):
        include_disabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountCollection]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        include_disabled=include_disabled,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    include_disabled: bool | Unset = UNSET,
) -> AccountCollection | None:
    """List accounts

    Args:
        page (int | Unset):
        per_page (int | Unset):
        include_disabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountCollection
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        include_disabled=include_disabled,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    include_disabled: bool | Unset = UNSET,
) -> Response[AccountCollection]:
    """List accounts

    Args:
        page (int | Unset):
        per_page (int | Unset):
        include_disabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AccountCollection]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        include_disabled=include_disabled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    include_disabled: bool | Unset = UNSET,
) -> AccountCollection | None:
    """List accounts

    Args:
        page (int | Unset):
        per_page (int | Unset):
        include_disabled (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AccountCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            include_disabled=include_disabled,
        )
    ).parsed
