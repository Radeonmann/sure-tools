from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.import_preflight_response import ImportPreflightResponse
from ...models.post_api_v1_imports_preflight_files_body import PostApiV1ImportsPreflightFilesBody
from ...models.post_api_v1_imports_preflight_json_body import PostApiV1ImportsPreflightJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApiV1ImportsPreflightJsonBody | PostApiV1ImportsPreflightFilesBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/imports/preflight",
    }

    if isinstance(body, PostApiV1ImportsPreflightJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostApiV1ImportsPreflightFilesBody):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ImportPreflightResponse | None:
    if response.status_code == 200:
        response_200 = ImportPreflightResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ImportPreflightResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiV1ImportsPreflightJsonBody | PostApiV1ImportsPreflightFilesBody | Unset = UNSET,
) -> Response[ErrorResponse | ImportPreflightResponse]:
    """Validate import content without creating an import

     Validate CSV or Sure NDJSON import content and return counts, headers, warnings, and validation
    errors without persisting an import or enqueueing jobs. CSV content is limited to 10MB.

    Args:
        body (PostApiV1ImportsPreflightJsonBody | Unset):
        body (PostApiV1ImportsPreflightFilesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ImportPreflightResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: PostApiV1ImportsPreflightJsonBody | PostApiV1ImportsPreflightFilesBody | Unset = UNSET,
) -> ErrorResponse | ImportPreflightResponse | None:
    """Validate import content without creating an import

     Validate CSV or Sure NDJSON import content and return counts, headers, warnings, and validation
    errors without persisting an import or enqueueing jobs. CSV content is limited to 10MB.

    Args:
        body (PostApiV1ImportsPreflightJsonBody | Unset):
        body (PostApiV1ImportsPreflightFilesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ImportPreflightResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiV1ImportsPreflightJsonBody | PostApiV1ImportsPreflightFilesBody | Unset = UNSET,
) -> Response[ErrorResponse | ImportPreflightResponse]:
    """Validate import content without creating an import

     Validate CSV or Sure NDJSON import content and return counts, headers, warnings, and validation
    errors without persisting an import or enqueueing jobs. CSV content is limited to 10MB.

    Args:
        body (PostApiV1ImportsPreflightJsonBody | Unset):
        body (PostApiV1ImportsPreflightFilesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ImportPreflightResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiV1ImportsPreflightJsonBody | PostApiV1ImportsPreflightFilesBody | Unset = UNSET,
) -> ErrorResponse | ImportPreflightResponse | None:
    """Validate import content without creating an import

     Validate CSV or Sure NDJSON import content and return counts, headers, warnings, and validation
    errors without persisting an import or enqueueing jobs. CSV content is limited to 10MB.

    Args:
        body (PostApiV1ImportsPreflightJsonBody | Unset):
        body (PostApiV1ImportsPreflightFilesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ImportPreflightResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
