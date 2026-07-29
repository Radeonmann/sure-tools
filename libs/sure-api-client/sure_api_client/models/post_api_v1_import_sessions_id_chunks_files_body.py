from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="PostApiV1ImportSessionsIdChunksFilesBody")


@_attrs_define
class PostApiV1ImportSessionsIdChunksFilesBody:
    """
    Attributes:
        sequence (int): One-based chunk sequence. Earlier dependency chunks must have lower sequence numbers.
        file (File): Multipart Sure NDJSON file upload. Each chunk is limited to 10MB.
        client_chunk_id (None | str | Unset): Client-provided idempotency key for this chunk.
    """

    sequence: int
    file: File
    client_chunk_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sequence = self.sequence

        file = self.file.to_tuple()

        client_chunk_id: None | str | Unset
        if isinstance(self.client_chunk_id, Unset):
            client_chunk_id = UNSET
        else:
            client_chunk_id = self.client_chunk_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sequence": sequence,
                "file": file,
            }
        )
        if client_chunk_id is not UNSET:
            field_dict["client_chunk_id"] = client_chunk_id

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("sequence", (None, str(self.sequence).encode(), "text/plain")))

        files.append(("file", self.file.to_tuple()))

        if not isinstance(self.client_chunk_id, Unset):
            if isinstance(self.client_chunk_id, str):
                files.append(("client_chunk_id", (None, str(self.client_chunk_id).encode(), "text/plain")))
            else:
                files.append(("client_chunk_id", (None, str(self.client_chunk_id).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sequence = d.pop("sequence")

        file = File(payload=BytesIO(d.pop("file")))

        def _parse_client_chunk_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_chunk_id = _parse_client_chunk_id(d.pop("client_chunk_id", UNSET))

        post_api_v1_import_sessions_id_chunks_files_body = cls(
            sequence=sequence,
            file=file,
            client_chunk_id=client_chunk_id,
        )

        post_api_v1_import_sessions_id_chunks_files_body.additional_properties = d
        return post_api_v1_import_sessions_id_chunks_files_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
