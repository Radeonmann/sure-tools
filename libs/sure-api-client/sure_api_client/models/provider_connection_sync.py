from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_connection_sync_latest import ProviderConnectionSyncLatest


T = TypeVar("T", bound="ProviderConnectionSync")


@_attrs_define
class ProviderConnectionSync:
    """
    Attributes:
        syncing (bool):
        status_summary (None | str | Unset):
        last_synced_at (datetime.datetime | None | Unset):
        latest (None | ProviderConnectionSyncLatest | Unset):
    """

    syncing: bool
    status_summary: None | str | Unset = UNSET
    last_synced_at: datetime.datetime | None | Unset = UNSET
    latest: None | ProviderConnectionSyncLatest | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.provider_connection_sync_latest import ProviderConnectionSyncLatest

        syncing = self.syncing

        status_summary: None | str | Unset
        if isinstance(self.status_summary, Unset):
            status_summary = UNSET
        else:
            status_summary = self.status_summary

        last_synced_at: None | str | Unset
        if isinstance(self.last_synced_at, Unset):
            last_synced_at = UNSET
        elif isinstance(self.last_synced_at, datetime.datetime):
            last_synced_at = self.last_synced_at.isoformat()
        else:
            last_synced_at = self.last_synced_at

        latest: dict[str, Any] | None | Unset
        if isinstance(self.latest, Unset):
            latest = UNSET
        elif isinstance(self.latest, ProviderConnectionSyncLatest):
            latest = self.latest.to_dict()
        else:
            latest = self.latest

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "syncing": syncing,
            }
        )
        if status_summary is not UNSET:
            field_dict["status_summary"] = status_summary
        if last_synced_at is not UNSET:
            field_dict["last_synced_at"] = last_synced_at
        if latest is not UNSET:
            field_dict["latest"] = latest

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_connection_sync_latest import ProviderConnectionSyncLatest

        d = dict(src_dict)
        syncing = d.pop("syncing")

        def _parse_status_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        status_summary = _parse_status_summary(d.pop("status_summary", UNSET))

        def _parse_last_synced_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_synced_at_type_0 = datetime.datetime.fromisoformat(data)

                return last_synced_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_synced_at = _parse_last_synced_at(d.pop("last_synced_at", UNSET))

        def _parse_latest(data: object) -> None | ProviderConnectionSyncLatest | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                latest_type_1 = ProviderConnectionSyncLatest.from_dict(data)

                return latest_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProviderConnectionSyncLatest | Unset, data)

        latest = _parse_latest(d.pop("latest", UNSET))

        provider_connection_sync = cls(
            syncing=syncing,
            status_summary=status_summary,
            last_synced_at=last_synced_at,
            latest=latest,
        )

        provider_connection_sync.additional_properties = d
        return provider_connection_sync

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
