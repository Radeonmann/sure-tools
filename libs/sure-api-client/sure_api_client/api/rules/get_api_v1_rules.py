from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_api_v1_rules_resource_type import GetApiV1RulesResourceType
from ...models.rule_collection import RuleCollection
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    resource_type: GetApiV1RulesResourceType | Unset = UNSET,
    active: bool | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["page"] = page

    params["per_page"] = per_page

    json_resource_type: str | Unset = UNSET
    if not isinstance(resource_type, Unset):
        json_resource_type = resource_type.value

    params["resource_type"] = json_resource_type

    params["active"] = active

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/rules",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | RuleCollection | None:
    if response.status_code == 200:
        response_200 = RuleCollection.from_dict(response.json())

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
) -> Response[ErrorResponse | RuleCollection]:
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
    resource_type: GetApiV1RulesResourceType | Unset = UNSET,
    active: bool | Unset = UNSET,
) -> Response[ErrorResponse | RuleCollection]:
    """List rules

    Args:
        page (int | Unset):
        per_page (int | Unset):
        resource_type (GetApiV1RulesResourceType | Unset):
        active (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | RuleCollection]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        resource_type=resource_type,
        active=active,
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
    resource_type: GetApiV1RulesResourceType | Unset = UNSET,
    active: bool | Unset = UNSET,
) -> ErrorResponse | RuleCollection | None:
    """List rules

    Args:
        page (int | Unset):
        per_page (int | Unset):
        resource_type (GetApiV1RulesResourceType | Unset):
        active (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | RuleCollection
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        resource_type=resource_type,
        active=active,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    resource_type: GetApiV1RulesResourceType | Unset = UNSET,
    active: bool | Unset = UNSET,
) -> Response[ErrorResponse | RuleCollection]:
    """List rules

    Args:
        page (int | Unset):
        per_page (int | Unset):
        resource_type (GetApiV1RulesResourceType | Unset):
        active (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | RuleCollection]
    """

    kwargs = _get_kwargs(
        page=page,
        per_page=per_page,
        resource_type=resource_type,
        active=active,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    page: int | Unset = UNSET,
    per_page: int | Unset = UNSET,
    resource_type: GetApiV1RulesResourceType | Unset = UNSET,
    active: bool | Unset = UNSET,
) -> ErrorResponse | RuleCollection | None:
    """List rules

    Args:
        page (int | Unset):
        per_page (int | Unset):
        resource_type (GetApiV1RulesResourceType | Unset):
        active (bool | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | RuleCollection
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            resource_type=resource_type,
            active=active,
        )
    ).parsed
