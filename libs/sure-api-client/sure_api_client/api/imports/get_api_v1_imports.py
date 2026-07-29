from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_v1_imports_status import GetApiV1ImportsStatus
from ...models.get_api_v1_imports_type import GetApiV1ImportsType
from ...models.import_collection import ImportCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    status: GetApiV1ImportsStatus | Unset = UNSET,
    type_: GetApiV1ImportsType | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/imports",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ImportCollection | None:
    if response.status_code == 200:
        response_200 = ImportCollection.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ImportCollection]:
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
    status: GetApiV1ImportsStatus | Unset = UNSET,
    type_: GetApiV1ImportsType | Unset = UNSET,
) -> Response[ImportCollection]:
    """List imports

     List all imports for the user's family with pagination and filtering.

    Args:
        page (int | Unset):
        per_page (int | Unset):
        status (GetApiV1ImportsStatus | Unset):
        type_ (GetApiV1ImportsType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImportCollection]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        status=status,
        type_=type_,
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
    status: GetApiV1ImportsStatus | Unset = UNSET,
    type_: GetApiV1ImportsType | Unset = UNSET,
) -> ImportCollection | None:
    """List imports

     List all imports for the user's family with pagination and filtering.

    Args:
        page (int | Unset):
        per_page (int | Unset):
        status (GetApiV1ImportsStatus | Unset):
        type_ (GetApiV1ImportsType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ImportCollection
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        status=status,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    status: GetApiV1ImportsStatus | Unset = UNSET,
    type_: GetApiV1ImportsType | Unset = UNSET,
) -> Response[ImportCollection]:
    """List imports

     List all imports for the user's family with pagination and filtering.

    Args:
        page (int | Unset):
        per_page (int | Unset):
        status (GetApiV1ImportsStatus | Unset):
        type_ (GetApiV1ImportsType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ImportCollection]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        status=status,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    status: GetApiV1ImportsStatus | Unset = UNSET,
    type_: GetApiV1ImportsType | Unset = UNSET,
) -> ImportCollection | None:
    """List imports

     List all imports for the user's family with pagination and filtering.

    Args:
        page (int | Unset):
        per_page (int | Unset):
        status (GetApiV1ImportsStatus | Unset):
        type_ (GetApiV1ImportsType | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ImportCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            status=status,
            type_=type_,
        )
    ).parsed
