from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.import_session_status import ImportSessionStatus
from ..models.import_session_type import ImportSessionType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_session_chunk import ImportSessionChunk
    from ..models.import_session_error_type_0 import ImportSessionErrorType0
    from ..models.import_session_summary import ImportSessionSummary


T = TypeVar("T", bound="ImportSession")


@_attrs_define
class ImportSession:
    """
    Attributes:
        id (UUID):
        type_ (ImportSessionType):
        status (ImportSessionStatus):
        chunks_count (int):
        summary (ImportSessionSummary):
        chunks (list[ImportSessionChunk]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        client_session_id (None | str | Unset):
        expected_chunks (int | None | Unset):
        error (ImportSessionErrorType0 | None | Unset):
    """

    id: UUID
    type_: ImportSessionType
    status: ImportSessionStatus
    chunks_count: int
    summary: ImportSessionSummary
    chunks: list[ImportSessionChunk]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    client_session_id: None | str | Unset = UNSET
    expected_chunks: int | None | Unset = UNSET
    error: ImportSessionErrorType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.import_session_error_type_0 import ImportSessionErrorType0

        id = str(self.id)

        type_ = self.type_.value

        status = self.status.value

        chunks_count = self.chunks_count

        summary = self.summary.to_dict()

        chunks = []
        for chunks_item_data in self.chunks:
            chunks_item = chunks_item_data.to_dict()
            chunks.append(chunks_item)

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        client_session_id: None | str | Unset
        if isinstance(self.client_session_id, Unset):
            client_session_id = UNSET
        else:
            client_session_id = self.client_session_id

        expected_chunks: int | None | Unset
        if isinstance(self.expected_chunks, Unset):
            expected_chunks = UNSET
        else:
            expected_chunks = self.expected_chunks

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, ImportSessionErrorType0):
            error = self.error.to_dict()
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "type": type_,
                "status": status,
                "chunks_count": chunks_count,
                "summary": summary,
                "chunks": chunks,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if client_session_id is not UNSET:
            field_dict["client_session_id"] = client_session_id
        if expected_chunks is not UNSET:
            field_dict["expected_chunks"] = expected_chunks
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_session_chunk import ImportSessionChunk
        from ..models.import_session_error_type_0 import ImportSessionErrorType0
        from ..models.import_session_summary import ImportSessionSummary

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        type_ = ImportSessionType(d.pop("type"))

        status = ImportSessionStatus(d.pop("status"))

        chunks_count = d.pop("chunks_count")

        summary = ImportSessionSummary.from_dict(d.pop("summary"))

        chunks = []
        _chunks = d.pop("chunks")
        for chunks_item_data in _chunks:
            chunks_item = ImportSessionChunk.from_dict(chunks_item_data)

            chunks.append(chunks_item)

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_client_session_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_session_id = _parse_client_session_id(d.pop("client_session_id", UNSET))

        def _parse_expected_chunks(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        expected_chunks = _parse_expected_chunks(d.pop("expected_chunks", UNSET))

        def _parse_error(data: object) -> ImportSessionErrorType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = ImportSessionErrorType0.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImportSessionErrorType0 | None | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        import_session = cls(
            id=id,
            type_=type_,
            status=status,
            chunks_count=chunks_count,
            summary=summary,
            chunks=chunks,
            created_at=created_at,
            updated_at=updated_at,
            client_session_id=client_session_id,
            expected_chunks=expected_chunks,
            error=error,
        )

        import_session.additional_properties = d
        return import_session

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
