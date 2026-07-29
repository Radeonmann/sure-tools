import datetime
from http import HTTPStatus
from typing import Any
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_v1_rule_runs_execution_type import GetApiV1RuleRunsExecutionType
from ...models.get_api_v1_rule_runs_status import GetApiV1RuleRunsStatus
from ...models.rule_run_collection import RuleRunCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    rule_id: UUID | Unset = UNSET,
    status: GetApiV1RuleRunsStatus | Unset = UNSET,
    execution_type: GetApiV1RuleRunsExecutionType | Unset = UNSET,
    start_executed_at: datetime.datetime | Unset = UNSET,
    end_executed_at: datetime.datetime | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    json_rule_id: str | Unset = UNSET
    if not isinstance(rule_id, Unset):
        json_rule_id = str(rule_id)
    params["rule_id"] = json_rule_id

    json_status: str | Unset = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_execution_type: str | Unset = UNSET
    if not isinstance(execution_type, Unset):
        json_execution_type = execution_type.value

    params["execution_type"] = json_execution_type

    json_start_executed_at: str | Unset = UNSET
    if not isinstance(start_executed_at, Unset):
        json_start_executed_at = start_executed_at.isoformat()
    params["start_executed_at"] = json_start_executed_at

    json_end_executed_at: str | Unset = UNSET
    if not isinstance(end_executed_at, Unset):
        json_end_executed_at = end_executed_at.isoformat()
    params["end_executed_at"] = json_end_executed_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/rule_runs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | RuleRunCollection | None:
    if response.status_code == 200:
        response_200 = RuleRunCollection.from_dict(response.json())

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
) -> Response[ErrorResponse | RuleRunCollection]:
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
    rule_id: UUID | Unset = UNSET,
    status: GetApiV1RuleRunsStatus | Unset = UNSET,
    execution_type: GetApiV1RuleRunsExecutionType | Unset = UNSET,
    start_executed_at: datetime.datetime | Unset = UNSET,
    end_executed_at: datetime.datetime | Unset = UNSET,
) -> Response[ErrorResponse | RuleRunCollection]:
    """List rule runs

     List rule run history for the authenticated user family.

    Args:
        page (int | Unset):
        per_page (int | Unset):
        rule_id (UUID | Unset):
        status (GetApiV1RuleRunsStatus | Unset):
        execution_type (GetApiV1RuleRunsExecutionType | Unset):
        start_executed_at (datetime.datetime | Unset):
        end_executed_at (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | RuleRunCollection]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        rule_id=rule_id,
        status=status,
        execution_type=execution_type,
        start_executed_at=start_executed_at,
        end_executed_at=end_executed_at,
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
    rule_id: UUID | Unset = UNSET,
    status: GetApiV1RuleRunsStatus | Unset = UNSET,
    execution_type: GetApiV1RuleRunsExecutionType | Unset = UNSET,
    start_executed_at: datetime.datetime | Unset = UNSET,
    end_executed_at: datetime.datetime | Unset = UNSET,
) -> ErrorResponse | RuleRunCollection | None:
    """List rule runs

     List rule run history for the authenticated user family.

    Args:
        page (int | Unset):
        per_page (int | Unset):
        rule_id (UUID | Unset):
        status (GetApiV1RuleRunsStatus | Unset):
        execution_type (GetApiV1RuleRunsExecutionType | Unset):
        start_executed_at (datetime.datetime | Unset):
        end_executed_at (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | RuleRunCollection
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        rule_id=rule_id,
        status=status,
        execution_type=execution_type,
        start_executed_at=start_executed_at,
        end_executed_at=end_executed_at,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    rule_id: UUID | Unset = UNSET,
    status: GetApiV1RuleRunsStatus | Unset = UNSET,
    execution_type: GetApiV1RuleRunsExecutionType | Unset = UNSET,
    start_executed_at: datetime.datetime | Unset = UNSET,
    end_executed_at: datetime.datetime | Unset = UNSET,
) -> Response[ErrorResponse | RuleRunCollection]:
    """List rule runs

     List rule run history for the authenticated user family.

    Args:
        page (int | Unset):
        per_page (int | Unset):
        rule_id (UUID | Unset):
        status (GetApiV1RuleRunsStatus | Unset):
        execution_type (GetApiV1RuleRunsExecutionType | Unset):
        start_executed_at (datetime.datetime | Unset):
        end_executed_at (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | RuleRunCollection]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        rule_id=rule_id,
        status=status,
        execution_type=execution_type,
        start_executed_at=start_executed_at,
        end_executed_at=end_executed_at,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    rule_id: UUID | Unset = UNSET,
    status: GetApiV1RuleRunsStatus | Unset = UNSET,
    execution_type: GetApiV1RuleRunsExecutionType | Unset = UNSET,
    start_executed_at: datetime.datetime | Unset = UNSET,
    end_executed_at: datetime.datetime | Unset = UNSET,
) -> ErrorResponse | RuleRunCollection | None:
    """List rule runs

     List rule run history for the authenticated user family.

    Args:
        page (int | Unset):
        per_page (int | Unset):
        rule_id (UUID | Unset):
        status (GetApiV1RuleRunsStatus | Unset):
        execution_type (GetApiV1RuleRunsExecutionType | Unset):
        start_executed_at (datetime.datetime | Unset):
        end_executed_at (datetime.datetime | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | RuleRunCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            rule_id=rule_id,
            status=status,
            execution_type=execution_type,
            start_executed_at=start_executed_at,
            end_executed_at=end_executed_at,
        )
    ).parsed
