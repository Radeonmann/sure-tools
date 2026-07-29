from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.import_session_response import ImportSessionResponse
from ...models.post_api_v1_import_sessions_id_chunks_files_body import PostApiV1ImportSessionsIdChunksFilesBody
from ...models.post_api_v1_import_sessions_id_chunks_json_body import PostApiV1ImportSessionsIdChunksJsonBody
from ...types import UNSET, Response


def _get_kwargs(
    id: str,
    *,
    body: PostApiV1ImportSessionsIdChunksJsonBody | PostApiV1ImportSessionsIdChunksFilesBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/api/v1/import_sessions/{id}/chunks".format(
            id=quote(str(id), safe=""),
        ),
    }

    if isinstance(body, PostApiV1ImportSessionsIdChunksJsonBody):
        _kwargs["json"] = body.to_dict()

        headers["Content-Type"] = "application/json"
    if isinstance(body, PostApiV1ImportSessionsIdChunksFilesBody):
        _kwargs["files"] = body.to_multipart()

        headers["Content-Type"] = "multipart/form-data; boundary=+++"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | ImportSessionResponse | None:
    if response.status_code == 201:
        response_201 = ImportSessionResponse.from_dict(response.json())

        return response_201

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = ErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | ImportSessionResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostApiV1ImportSessionsIdChunksJsonBody | PostApiV1ImportSessionsIdChunksFilesBody | Unset = UNSET,
) -> Response[ErrorResponse | ImportSessionResponse]:
    """Upload import session chunk

     Attach an ordered Sure NDJSON chunk to an import session. Chunks are idempotent by sequence and
    client_chunk_id with content verification.

    Args:
        id (str):
        body (PostApiV1ImportSessionsIdChunksJsonBody):
        body (PostApiV1ImportSessionsIdChunksFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ImportSessionResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostApiV1ImportSessionsIdChunksJsonBody | PostApiV1ImportSessionsIdChunksFilesBody | Unset = UNSET,
) -> ErrorResponse | ImportSessionResponse | None:
    """Upload import session chunk

     Attach an ordered Sure NDJSON chunk to an import session. Chunks are idempotent by sequence and
    client_chunk_id with content verification.

    Args:
        id (str):
        body (PostApiV1ImportSessionsIdChunksJsonBody):
        body (PostApiV1ImportSessionsIdChunksFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ImportSessionResponse
    """

    return sync_detailed(
        id=id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostApiV1ImportSessionsIdChunksJsonBody | PostApiV1ImportSessionsIdChunksFilesBody | Unset = UNSET,
) -> Response[ErrorResponse | ImportSessionResponse]:
    """Upload import session chunk

     Attach an ordered Sure NDJSON chunk to an import session. Chunks are idempotent by sequence and
    client_chunk_id with content verification.

    Args:
        id (str):
        body (PostApiV1ImportSessionsIdChunksJsonBody):
        body (PostApiV1ImportSessionsIdChunksFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | ImportSessionResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    body: PostApiV1ImportSessionsIdChunksJsonBody | PostApiV1ImportSessionsIdChunksFilesBody | Unset = UNSET,
) -> ErrorResponse | ImportSessionResponse | None:
    """Upload import session chunk

     Attach an ordered Sure NDJSON chunk to an import session. Chunks are idempotent by sequence and
    client_chunk_id with content verification.

    Args:
        id (str):
        body (PostApiV1ImportSessionsIdChunksJsonBody):
        body (PostApiV1ImportSessionsIdChunksFilesBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | ImportSessionResponse
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            body=body,
        )
    ).parsed
