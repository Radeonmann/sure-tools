from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_v1_recurring_transactions_status import GetApiV1RecurringTransactionsStatus
from ...models.recurring_transaction_collection import RecurringTransactionCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    status: GetApiV1RecurringTransactionsStatus | Unset = UNSET,
    account_id: UUID | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_account_id: str | Unset = UNSET
    if not isinstance(account_id, Unset):
        json_account_id = str(account_id)
    params["account_id"] = json_account_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/recurring_transactions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | RecurringTransactionCollection | None:
    if response.status_code == 200:
        response_200 = RecurringTransactionCollection.from_dict(response.json())

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
) -> Response[ErrorResponse | RecurringTransactionCollection]:
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
    status: GetApiV1RecurringTransactionsStatus | Unset = UNSET,
    account_id: UUID | Unset = UNSET,
) -> Response[ErrorResponse | RecurringTransactionCollection]:
    """List recurring transactions

    Args:
        page (int | Unset):
        per_page (int | Unset):
        status (GetApiV1RecurringTransactionsStatus | Unset):
        account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | RecurringTransactionCollection]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        status=status,
        account_id=account_id,
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
    status: GetApiV1RecurringTransactionsStatus | Unset = UNSET,
    account_id: UUID | Unset = UNSET,
) -> ErrorResponse | RecurringTransactionCollection | None:
    """List recurring transactions

    Args:
        page (int | Unset):
        per_page (int | Unset):
        status (GetApiV1RecurringTransactionsStatus | Unset):
        account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | RecurringTransactionCollection
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        status=status,
        account_id=account_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    status: GetApiV1RecurringTransactionsStatus | Unset = UNSET,
    account_id: UUID | Unset = UNSET,
) -> Response[ErrorResponse | RecurringTransactionCollection]:
    """List recurring transactions

    Args:
        page (int | Unset):
        per_page (int | Unset):
        status (GetApiV1RecurringTransactionsStatus | Unset):
        account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | RecurringTransactionCollection]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        status=status,
        account_id=account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    status: GetApiV1RecurringTransactionsStatus | Unset = UNSET,
    account_id: UUID | Unset = UNSET,
) -> ErrorResponse | RecurringTransactionCollection | None:
    """List recurring transactions

    Args:
        page (int | Unset):
        per_page (int | Unset):
        status (GetApiV1RecurringTransactionsStatus | Unset):
        account_id (UUID | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | RecurringTransactionCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            status=status,
            account_id=account_id,
        )
    ).parsed
