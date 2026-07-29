import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.trade_collection import TradeCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    account_id: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["account_id"] = account_id

    json_account_ids: list[str] | Unset = UNSET
    if not isinstance(account_ids, Unset):
        json_account_ids = account_ids

    params["account_ids"] = json_account_ids

    json_start_date: str | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_end_date: str | Unset = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/trades",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | TradeCollection | None:
    if response.status_code == 200:
        response_200 = TradeCollection.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | TradeCollection]:
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
    account_id: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
) -> Response[ErrorResponse | TradeCollection]:
    """List trades

    Args:
        page (int | Unset):
        per_page (int | Unset):
        account_id (str | Unset):
        account_ids (list[str] | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TradeCollection]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        account_id=account_id,
        account_ids=account_ids,
        start_date=start_date,
        end_date=end_date,
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
    account_id: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
) -> ErrorResponse | TradeCollection | None:
    """List trades

    Args:
        page (int | Unset):
        per_page (int | Unset):
        account_id (str | Unset):
        account_ids (list[str] | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TradeCollection
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        account_id=account_id,
        account_ids=account_ids,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    account_id: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
) -> Response[ErrorResponse | TradeCollection]:
    """List trades

    Args:
        page (int | Unset):
        per_page (int | Unset):
        account_id (str | Unset):
        account_ids (list[str] | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | TradeCollection]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        account_id=account_id,
        account_ids=account_ids,
        start_date=start_date,
        end_date=end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    account_id: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
) -> ErrorResponse | TradeCollection | None:
    """List trades

    Args:
        page (int | Unset):
        per_page (int | Unset):
        account_id (str | Unset):
        account_ids (list[str] | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | TradeCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            account_id=account_id,
            account_ids=account_ids,
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed
