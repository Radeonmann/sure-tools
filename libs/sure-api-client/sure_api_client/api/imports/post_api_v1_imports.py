from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.error_response_with_import_id import ErrorResponseWithImportId
from ...models.import_response import ImportResponse
from ...models.post_api_v1_imports_files_body import PostApiV1ImportsFilesBody
from ...models.post_api_v1_imports_json_body import PostApiV1ImportsJsonBody
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostApiV1ImportsJsonBody | PostApiV1ImportsFilesBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/imports",
    }

    if isinstance(body, PostApiV1ImportsJsonBody):
        if not isinstance(body, Unset):
            _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostApiV1ImportsFilesBody):
        if not isinstance(body, Unset):
            _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ErrorResponseWithImportId | ErrorResponseWithImportId | ImportResponse | None:
    if response.status_code == 201:
        response_201 = ImportResponse.from_dict(response.json())

        return response_201

    if response.status_code == 422:

        def _parse_response_422(data: object) -> ErrorResponse | ErrorResponseWithImportId:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_422_type_0 = ErrorResponse.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_1 = ErrorResponseWithImportId.from_dict(data)

            return response_422_type_1

        response_422 = _parse_response_422(response.json())

        return response_422

    if response.status_code == 500:
        response_500 = ErrorResponseWithImportId.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ErrorResponseWithImportId | ErrorResponseWithImportId | ImportResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiV1ImportsJsonBody | PostApiV1ImportsFilesBody | Unset = UNSET,
) -> Response[ErrorResponse | ErrorResponseWithImportId | ErrorResponseWithImportId | ImportResponse]:
    """Create import

     Create a new import from raw CSV content, inline Sure NDJSON content, or an uploaded Sure NDJSON
    file. CSV content is limited to 10MB.

    Args:
        body (PostApiV1ImportsJsonBody | Unset):
        body (PostApiV1ImportsFilesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ErrorResponseWithImportId | ErrorResponseWithImportId | ImportResponse]
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
    body: PostApiV1ImportsJsonBody | PostApiV1ImportsFilesBody | Unset = UNSET,
) -> ErrorResponse | ErrorResponseWithImportId | ErrorResponseWithImportId | ImportResponse | None:
    """Create import

     Create a new import from raw CSV content, inline Sure NDJSON content, or an uploaded Sure NDJSON
    file. CSV content is limited to 10MB.

    Args:
        body (PostApiV1ImportsJsonBody | Unset):
        body (PostApiV1ImportsFilesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ErrorResponseWithImportId | ErrorResponseWithImportId | ImportResponse
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostApiV1ImportsJsonBody | PostApiV1ImportsFilesBody | Unset = UNSET,
) -> Response[ErrorResponse | ErrorResponseWithImportId | ErrorResponseWithImportId | ImportResponse]:
    """Create import

     Create a new import from raw CSV content, inline Sure NDJSON content, or an uploaded Sure NDJSON
    file. CSV content is limited to 10MB.

    Args:
        body (PostApiV1ImportsJsonBody | Unset):
        body (PostApiV1ImportsFilesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ErrorResponseWithImportId | ErrorResponseWithImportId | ImportResponse]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostApiV1ImportsJsonBody | PostApiV1ImportsFilesBody | Unset = UNSET,
) -> ErrorResponse | ErrorResponseWithImportId | ErrorResponseWithImportId | ImportResponse | None:
    """Create import

     Create a new import from raw CSV content, inline Sure NDJSON content, or an uploaded Sure NDJSON
    file. CSV content is limited to 10MB.

    Args:
        body (PostApiV1ImportsJsonBody | Unset):
        body (PostApiV1ImportsFilesBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ErrorResponseWithImportId | ErrorResponseWithImportId | ImportResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
