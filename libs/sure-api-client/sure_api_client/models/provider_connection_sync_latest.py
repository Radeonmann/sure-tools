from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_connection_sync_latest_error_type_0 import ProviderConnectionSyncLatestErrorType0


T = TypeVar("T", bound="ProviderConnectionSyncLatest")


@_attrs_define
class ProviderConnectionSyncLatest:
    """
    Attributes:
        id (UUID):
        status (str):
        created_at (datetime.datetime):
        syncing_at (datetime.datetime | None | Unset):
        completed_at (datetime.datetime | None | Unset):
        failed_at (datetime.datetime | None | Unset):
        error (None | ProviderConnectionSyncLatestErrorType0 | Unset): Sanitized latest sync error summary. Null when
            the latest sync is not failed or stale.
    """

    id: UUID
    status: str
    created_at: datetime.datetime
    syncing_at: datetime.datetime | None | Unset = UNSET
    completed_at: datetime.datetime | None | Unset = UNSET
    failed_at: datetime.datetime | None | Unset = UNSET
    error: None | ProviderConnectionSyncLatestErrorType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_connection_sync_latest_error_type_0 import ProviderConnectionSyncLatestErrorType0

        id = str(self.id)

        status = self.status

        created_at = self.created_at.isoformat()

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
        elif isinstance(self.error, ProviderConnectionSyncLatestErrorType0):
            error = self.error.to_dict()
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "status": status,
                "created_at": created_at,
            }
        )
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
        from ..models.provider_connection_sync_latest_error_type_0 import ProviderConnectionSyncLatestErrorType0

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        status = d.pop("status")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

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

        def _parse_error(data: object) -> None | ProviderConnectionSyncLatestErrorType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                error_type_0 = ProviderConnectionSyncLatestErrorType0.from_dict(data)

                return error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProviderConnectionSyncLatestErrorType0 | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        provider_connection_sync_latest = cls(
            id=id,
            status=status,
            created_at=created_at,
            syncing_at=syncing_at,
            completed_at=completed_at,
            failed_at=failed_at,
            error=error,
        )

        provider_connection_sync_latest.additional_properties = d
        return provider_connection_sync_latest

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
