from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.category_collection import CategoryCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    roots_only: bool | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["roots_only"] = roots_only

    json_parent_id: str | Unset = UNSET
    if not isinstance(parent_id, Unset):
        json_parent_id = str(parent_id)
    params["parent_id"] = json_parent_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/categories",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> CategoryCollection | None:
    if response.status_code == 200:
        response_200 = CategoryCollection.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[CategoryCollection]:
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
    roots_only: bool | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
) -> Response[CategoryCollection]:
    """List categories

    Args:
        page (int | Unset):
        per_page (int | Unset):
        roots_only (bool | Unset):
        parent_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CategoryCollection]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        roots_only=roots_only,
        parent_id=parent_id,
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
    roots_only: bool | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
) -> CategoryCollection | None:
    """List categories

    Args:
        page (int | Unset):
        per_page (int | Unset):
        roots_only (bool | Unset):
        parent_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CategoryCollection
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        roots_only=roots_only,
        parent_id=parent_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    roots_only: bool | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
) -> Response[CategoryCollection]:
    """List categories

    Args:
        page (int | Unset):
        per_page (int | Unset):
        roots_only (bool | Unset):
        parent_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CategoryCollection]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        roots_only=roots_only,
        parent_id=parent_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    roots_only: bool | Unset = UNSET,
    parent_id: UUID | Unset = UNSET,
) -> CategoryCollection | None:
    """List categories

    Args:
        page (int | Unset):
        per_page (int | Unset):
        roots_only (bool | Unset):
        parent_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CategoryCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            roots_only=roots_only,
            parent_id=parent_id,
        )
    ).parsed
