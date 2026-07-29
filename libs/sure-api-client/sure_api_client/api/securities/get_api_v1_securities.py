from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_v1_securities_kind import GetApiV1SecuritiesKind
from ...models.security_collection import SecurityCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    ticker: str | Unset = UNSET,
    exchange_operating_mic: str | Unset = UNSET,
    kind: GetApiV1SecuritiesKind | Unset = UNSET,
    offline: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["ticker"] = ticker

    params["exchange_operating_mic"] = exchange_operating_mic

    json_kind: str | Unset = UNSET
    if not isinstance(kind, Unset):
        json_kind = kind.value

    params["kind"] = json_kind

    params["offline"] = offline

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/securities",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | SecurityCollection | None:
    if response.status_code == 200:
        response_200 = SecurityCollection.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | SecurityCollection]:
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
    ticker: str | Unset = UNSET,
    exchange_operating_mic: str | Unset = UNSET,
    kind: GetApiV1SecuritiesKind | Unset = UNSET,
    offline: bool | Unset = UNSET,
) -> Response[ErrorResponse | SecurityCollection]:
    """List securities referenced by family investment data

    Args:
        page (int | Unset):
        per_page (int | Unset):
        ticker (str | Unset):
        exchange_operating_mic (str | Unset):
        kind (GetApiV1SecuritiesKind | Unset):
        offline (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SecurityCollection]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        ticker=ticker,
        exchange_operating_mic=exchange_operating_mic,
        kind=kind,
        offline=offline,
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
    ticker: str | Unset = UNSET,
    exchange_operating_mic: str | Unset = UNSET,
    kind: GetApiV1SecuritiesKind | Unset = UNSET,
    offline: bool | Unset = UNSET,
) -> ErrorResponse | SecurityCollection | None:
    """List securities referenced by family investment data

    Args:
        page (int | Unset):
        per_page (int | Unset):
        ticker (str | Unset):
        exchange_operating_mic (str | Unset):
        kind (GetApiV1SecuritiesKind | Unset):
        offline (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SecurityCollection
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        ticker=ticker,
        exchange_operating_mic=exchange_operating_mic,
        kind=kind,
        offline=offline,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    ticker: str | Unset = UNSET,
    exchange_operating_mic: str | Unset = UNSET,
    kind: GetApiV1SecuritiesKind | Unset = UNSET,
    offline: bool | Unset = UNSET,
) -> Response[ErrorResponse | SecurityCollection]:
    """List securities referenced by family investment data

    Args:
        page (int | Unset):
        per_page (int | Unset):
        ticker (str | Unset):
        exchange_operating_mic (str | Unset):
        kind (GetApiV1SecuritiesKind | Unset):
        offline (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | SecurityCollection]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        ticker=ticker,
        exchange_operating_mic=exchange_operating_mic,
        kind=kind,
        offline=offline,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    ticker: str | Unset = UNSET,
    exchange_operating_mic: str | Unset = UNSET,
    kind: GetApiV1SecuritiesKind | Unset = UNSET,
    offline: bool | Unset = UNSET,
) -> ErrorResponse | SecurityCollection | None:
    """List securities referenced by family investment data

    Args:
        page (int | Unset):
        per_page (int | Unset):
        ticker (str | Unset):
        exchange_operating_mic (str | Unset):
        kind (GetApiV1SecuritiesKind | Unset):
        offline (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | SecurityCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            ticker=ticker,
            exchange_operating_mic=exchange_operating_mic,
            kind=kind,
            offline=offline,
        )
    ).parsed
