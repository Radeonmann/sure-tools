from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sync_resource_status import SyncResourceStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.sync_error_summary import SyncErrorSummary
    from ..models.syncable_summary import SyncableSummary


T = TypeVar("T", bound="SyncResource")


@_attrs_define
class SyncResource:
    """
    Attributes:
        id (UUID):
        status (SyncResourceStatus):
        in_progress (bool):
        terminal (bool):
        syncable (SyncableSummary):
        children_count (int):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        parent_id (None | Unset | UUID):
        window_start_date (datetime.date | None | Unset):
        window_end_date (datetime.date | None | Unset):
        pending_at (datetime.datetime | None | Unset):
        syncing_at (datetime.datetime | None | Unset):
        completed_at (datetime.datetime | None | Unset):
        failed_at (datetime.datetime | None | Unset):
        error (None | SyncErrorSummary | Unset):
    """

    id: UUID
    status: SyncResourceStatus
    in_progress: bool
    terminal: bool
    syncable: SyncableSummary
    children_count: int
    created_at: datetime.datetime
    updated_at: datetime.datetime
    parent_id: None | Unset | UUID = UNSET
    window_start_date: datetime.date | None | Unset = UNSET
    window_end_date: datetime.date | None | Unset = UNSET
    pending_at: datetime.datetime | None | Unset = UNSET
    syncing_at: datetime.datetime | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    failed_at: datetime.datetime | None | Unset = UNSET
    error: None | SyncErrorSummary | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.sync_error_summary import SyncErrorSummary

        id = str(self.id)

        status = self.status.value

        in_progress = self.in_progress

        terminal = self.terminal

        syncable = self.syncable.to_dict()

        children_count = self.children_count

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        parent_id: None | str | Unset
        if isinstance(self.parent_id, Unset):
            parent_id = UNSET
        elif isinstance(self.parent_id, UUID):
            parent_id = str(self.parent_id)
        else:
            parent_id = self.parent_id

        window_start_date: None | str | Unset
        if isinstance(self.window_start_date, Unset):
            window_start_date = UNSET
        elif isinstance(self.window_start_date, datetime.date):
            window_start_date = self.window_start_date.isoformat()
        else:
            window_start_date = self.window_start_date

        window_end_date: None | str | Unset
        if isinstance(self.window_end_date, Unset):
            window_end_date = UNSET
        elif isinstance(self.window_end_date, datetime.date):
            window_end_date = self.window_end_date.isoformat()
        else:
            window_end_date = self.window_end_date

        pending_at: None | str | Unset
        if isinstance(self.pending_at, Unset):
            pending_at = UNSET
        elif isinstance(self.pending_at, datetime.datetime):
            pending_at = self.pending_at.isoformat()
        else:
            pending_at = self.pending_at

        syncing_at: None | str | Unset
        if isinstance(self.syncing_at, Unset):
            syncing_at = UNSET
        elif isinstance(self.syncing_at, datetime.datetime):
            syncing_at = self.syncing_at.isoformat()
        else:
            syncing_at = self.syncing_at

        completed_at: None | str | Unset
        if isinstance(self.completed_at, Unset):
            completed_at = UNSET
        elif isinstance(self.completed_at, datetime.datetime):
            completed_at = self.completed_at.isoformat()
        else:
            completed_at = self.completed_at

        failed_at: None | str | Unset
        if isinstance(self.failed_at, Unset):
            failed_at = UNSET
        elif isinstance(self.failed_at, datetime.datetime):
            failed_at = self.failed_at.isoformat()
        else:
            failed_at = self.failed_at

        error: dict[str, Any] | None | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        elif isinstance(self.error, SyncErrorSummary):
            error = self.error.to_dict()
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "in_progress": in_progress,
                "terminal": terminal,
                "syncable": syncable,
                "children_count": children_count,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if window_start_date is not UNSET:
            field_dict["window_start_date"] = window_start_date
        if window_end_date is not UNSET:
            field_dict["window_end_date"] = window_end_date
        if pending_at is not UNSET:
            field_dict["pending_at"] = pending_at
        if syncing_at is not UNSET:
            field_dict["syncing_at"] = syncing_at
        if completed_at is not UNSET:
            field_dict["completed_at"] = completed_at
        if failed_at is not UNSET:
            field_dict["failed_at"] = failed_at
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sync_error_summary import SyncErrorSummary
        from ..models.syncable_summary import SyncableSummary

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = SyncResourceStatus(d.pop("status"))

        in_progress = d.pop("in_progress")

        terminal = d.pop("terminal")

        syncable = SyncableSummary.from_dict(d.pop("syncable"))

        children_count = d.pop("children_count")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_parent_id(data: object) -> None | Unset | UUID:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                parent_id_type_0 = UUID(data)

                return parent_id_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | UUID, data)

        parent_id = _parse_parent_id(d.pop("parent_id", UNSET))

        def _parse_window_start_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                window_start_date_type_0 = datetime.date.fromisoformat(data)

                return window_start_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        window_start_date = _parse_window_start_date(d.pop("window_start_date", UNSET))

        def _parse_window_end_date(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                window_end_date_type_0 = datetime.date.fromisoformat(data)

                return window_end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        window_end_date = _parse_window_end_date(d.pop("window_end_date", UNSET))

        def _parse_pending_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                pending_at_type_0 = datetime.datetime.fromisoformat(data)

                return pending_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        pending_at = _parse_pending_at(d.pop("pending_at", UNSET))

        def _parse_syncing_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                syncing_at_type_0 = datetime.datetime.fromisoformat(data)

                return syncing_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        syncing_at = _parse_syncing_at(d.pop("syncing_at", UNSET))

        def _parse_completed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                completed_at_type_0 = datetime.datetime.fromisoformat(data)

                return completed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        completed_at = _parse_completed_at(d.pop("completed_at", UNSET))

        def _parse_failed_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                failed_at_type_0 = datetime.datetime.fromisoformat(data)

                return failed_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        failed_at = _parse_failed_at(d.pop("failed_at", UNSET))

        def _parse_error(data: object) -> None | SyncErrorSummary | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_1 = SyncErrorSummary.from_dict(data)

                return error_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SyncErrorSummary | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        sync_resource = cls(
            id=id,
            status=status,
            in_progress=in_progress,
            terminal=terminal,
            syncable=syncable,
            children_count=children_count,
            created_at=created_at,
            updated_at=updated_at,
            parent_id=parent_id,
            window_start_date=window_start_date,
            window_end_date=window_end_date,
            pending_at=pending_at,
            syncing_at=syncing_at,
            completed_at=completed_at,
            failed_at=failed_at,
            error=error,
        )

        sync_resource.additional_properties = d
        return sync_resource

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
