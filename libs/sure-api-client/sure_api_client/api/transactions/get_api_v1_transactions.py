import datetime
from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_api_v1_transactions_type import GetApiV1TransactionsType
from ...models.transaction_collection import TransactionCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    account_id: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    merchant_id: str | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    min_amount: float | Unset = UNSET,
    max_amount: float | Unset = UNSET,
    type_: GetApiV1TransactionsType | Unset = UNSET,
    search: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    category_ids: list[str] | Unset = UNSET,
    merchant_ids: list[str] | Unset = UNSET,
    tag_ids: list[str] | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    params["account_id"] = account_id

    params["category_id"] = category_id

    params["merchant_id"] = merchant_id

    json_start_date: str | Unset = UNSET
    if not isinstance(start_date, Unset):
        json_start_date = start_date.isoformat()
    params["start_date"] = json_start_date

    json_end_date: str | Unset = UNSET
    if not isinstance(end_date, Unset):
        json_end_date = end_date.isoformat()
    params["end_date"] = json_end_date

    params["min_amount"] = min_amount

    params["max_amount"] = max_amount

    json_type_: str | Unset = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params["search"] = search

    json_account_ids: list[str] | Unset = UNSET
    if not isinstance(account_ids, Unset):
        json_account_ids = account_ids

    params["account_ids"] = json_account_ids

    json_category_ids: list[str] | Unset = UNSET
    if not isinstance(category_ids, Unset):
        json_category_ids = category_ids

    params["category_ids"] = json_category_ids

    json_merchant_ids: list[str] | Unset = UNSET
    if not isinstance(merchant_ids, Unset):
        json_merchant_ids = merchant_ids

    params["merchant_ids"] = json_merchant_ids

    json_tag_ids: list[str] | Unset = UNSET
    if not isinstance(tag_ids, Unset):
        json_tag_ids = tag_ids

    params["tag_ids"] = json_tag_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/transactions",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> TransactionCollection | None:
    if response.status_code == 200:
        response_200 = TransactionCollection.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[TransactionCollection]:
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
    category_id: str | Unset = UNSET,
    merchant_id: str | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    min_amount: float | Unset = UNSET,
    max_amount: float | Unset = UNSET,
    type_: GetApiV1TransactionsType | Unset = UNSET,
    search: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    category_ids: list[str] | Unset = UNSET,
    merchant_ids: list[str] | Unset = UNSET,
    tag_ids: list[str] | Unset = UNSET,
) -> Response[TransactionCollection]:
    """List transactions

     Returns global ledger history for accessible accounts, including disabled accounts but excluding
    accounts pending deletion.

    Args:
        page (int | Unset):
        per_page (int | Unset):
        account_id (str | Unset):
        category_id (str | Unset):
        merchant_id (str | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        min_amount (float | Unset):
        max_amount (float | Unset):
        type_ (GetApiV1TransactionsType | Unset):
        search (str | Unset):
        account_ids (list[str] | Unset):
        category_ids (list[str] | Unset):
        merchant_ids (list[str] | Unset):
        tag_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionCollection]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        account_id=account_id,
        category_id=category_id,
        merchant_id=merchant_id,
        start_date=start_date,
        end_date=end_date,
        min_amount=min_amount,
        max_amount=max_amount,
        type_=type_,
        search=search,
        account_ids=account_ids,
        category_ids=category_ids,
        merchant_ids=merchant_ids,
        tag_ids=tag_ids,
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
    category_id: str | Unset = UNSET,
    merchant_id: str | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    min_amount: float | Unset = UNSET,
    max_amount: float | Unset = UNSET,
    type_: GetApiV1TransactionsType | Unset = UNSET,
    search: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    category_ids: list[str] | Unset = UNSET,
    merchant_ids: list[str] | Unset = UNSET,
    tag_ids: list[str] | Unset = UNSET,
) -> TransactionCollection | None:
    """List transactions

     Returns global ledger history for accessible accounts, including disabled accounts but excluding
    accounts pending deletion.

    Args:
        page (int | Unset):
        per_page (int | Unset):
        account_id (str | Unset):
        category_id (str | Unset):
        merchant_id (str | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        min_amount (float | Unset):
        max_amount (float | Unset):
        type_ (GetApiV1TransactionsType | Unset):
        search (str | Unset):
        account_ids (list[str] | Unset):
        category_ids (list[str] | Unset):
        merchant_ids (list[str] | Unset):
        tag_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionCollection
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        account_id=account_id,
        category_id=category_id,
        merchant_id=merchant_id,
        start_date=start_date,
        end_date=end_date,
        min_amount=min_amount,
        max_amount=max_amount,
        type_=type_,
        search=search,
        account_ids=account_ids,
        category_ids=category_ids,
        merchant_ids=merchant_ids,
        tag_ids=tag_ids,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    account_id: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    merchant_id: str | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    min_amount: float | Unset = UNSET,
    max_amount: float | Unset = UNSET,
    type_: GetApiV1TransactionsType | Unset = UNSET,
    search: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    category_ids: list[str] | Unset = UNSET,
    merchant_ids: list[str] | Unset = UNSET,
    tag_ids: list[str] | Unset = UNSET,
) -> Response[TransactionCollection]:
    """List transactions

     Returns global ledger history for accessible accounts, including disabled accounts but excluding
    accounts pending deletion.

    Args:
        page (int | Unset):
        per_page (int | Unset):
        account_id (str | Unset):
        category_id (str | Unset):
        merchant_id (str | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        min_amount (float | Unset):
        max_amount (float | Unset):
        type_ (GetApiV1TransactionsType | Unset):
        search (str | Unset):
        account_ids (list[str] | Unset):
        category_ids (list[str] | Unset):
        merchant_ids (list[str] | Unset):
        tag_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[TransactionCollection]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        account_id=account_id,
        category_id=category_id,
        merchant_id=merchant_id,
        start_date=start_date,
        end_date=end_date,
        min_amount=min_amount,
        max_amount=max_amount,
        type_=type_,
        search=search,
        account_ids=account_ids,
        category_ids=category_ids,
        merchant_ids=merchant_ids,
        tag_ids=tag_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    account_id: str | Unset = UNSET,
    category_id: str | Unset = UNSET,
    merchant_id: str | Unset = UNSET,
    start_date: datetime.date | Unset = UNSET,
    end_date: datetime.date | Unset = UNSET,
    min_amount: float | Unset = UNSET,
    max_amount: float | Unset = UNSET,
    type_: GetApiV1TransactionsType | Unset = UNSET,
    search: str | Unset = UNSET,
    account_ids: list[str] | Unset = UNSET,
    category_ids: list[str] | Unset = UNSET,
    merchant_ids: list[str] | Unset = UNSET,
    tag_ids: list[str] | Unset = UNSET,
) -> TransactionCollection | None:
    """List transactions

     Returns global ledger history for accessible accounts, including disabled accounts but excluding
    accounts pending deletion.

    Args:
        page (int | Unset):
        per_page (int | Unset):
        account_id (str | Unset):
        category_id (str | Unset):
        merchant_id (str | Unset):
        start_date (datetime.date | Unset):
        end_date (datetime.date | Unset):
        min_amount (float | Unset):
        max_amount (float | Unset):
        type_ (GetApiV1TransactionsType | Unset):
        search (str | Unset):
        account_ids (list[str] | Unset):
        category_ids (list[str] | Unset):
        merchant_ids (list[str] | Unset):
        tag_ids (list[str] | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        TransactionCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            account_id=account_id,
            category_id=category_id,
            merchant_id=merchant_id,
            start_date=start_date,
            end_date=end_date,
            min_amount=min_amount,
            max_amount=max_amount,
            type_=type_,
            search=search,
            account_ids=account_ids,
            category_ids=category_ids,
            merchant_ids=merchant_ids,
            tag_ids=tag_ids,
        )
    ).parsed
