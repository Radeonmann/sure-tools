from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.import_session_chunk_status import ImportSessionChunkStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.import_session_chunk_error_type_0 import ImportSessionChunkErrorType0
    from ..models.import_session_chunk_summary import ImportSessionChunkSummary


T = TypeVar("T", bound="ImportSessionChunk")


@_attrs_define
class ImportSessionChunk:
    """
    Attributes:
        id (UUID):
        sequence (int):
        status (ImportSessionChunkStatus):
        rows_count (int):
        summary (ImportSessionChunkSummary):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        client_chunk_id (None | str | Unset):
        error (ImportSessionChunkErrorType0 | None | Unset):
    """

    id: UUID
    sequence: int
    status: ImportSessionChunkStatus
    rows_count: int
    summary: ImportSessionChunkSummary
    created_at: datetime.datetime
    updated_at: datetime.datetime
    client_chunk_id: None | str | Unset = UNSET
    error: ImportSessionChunkErrorType0 | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.import_session_chunk_error_type_0 import ImportSessionChunkErrorType0

        id = str(self.id)

        sequence = self.sequence

        status = self.status.value

        rows_count = self.rows_count

        summary = self.summary.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        client_chunk_id: None | str | Unset
        if isinstance(self.client_chunk_id, Unset):
            client_chunk_id = UNSET
        else:
            client_chunk_id = self.client_chunk_id

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, ImportSessionChunkErrorType0):
            error = self.error.to_dict()
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "sequence": sequence,
                "status": status,
                "rows_count": rows_count,
                "summary": summary,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if client_chunk_id is not UNSET:
            field_dict["client_chunk_id"] = client_chunk_id
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.import_session_chunk_error_type_0 import ImportSessionChunkErrorType0
        from ..models.import_session_chunk_summary import ImportSessionChunkSummary

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        sequence = d.pop("sequence")

        status = ImportSessionChunkStatus(d.pop("status"))

        rows_count = d.pop("rows_count")

        summary = ImportSessionChunkSummary.from_dict(d.pop("summary"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_client_chunk_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_chunk_id = _parse_client_chunk_id(d.pop("client_chunk_id", UNSET))

        def _parse_error(data: object) -> ImportSessionChunkErrorType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = ImportSessionChunkErrorType0.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ImportSessionChunkErrorType0 | None | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        import_session_chunk = cls(
            id=id,
            sequence=sequence,
            status=status,
            rows_count=rows_count,
            summary=summary,
            created_at=created_at,
            updated_at=updated_at,
            client_chunk_id=client_chunk_id,
            error=error,
        )

        import_session_chunk.additional_properties = d
        return import_session_chunk

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
