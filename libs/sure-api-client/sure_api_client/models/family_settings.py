from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.family_settings_default_account_sharing import FamilySettingsDefaultAccountSharing
from ..models.family_settings_moniker import FamilySettingsMoniker
from ..types import UNSET, Unset

T = TypeVar("T", bound="FamilySettings")


@_attrs_define
class FamilySettings:
    """
    Attributes:
        id (UUID):
        currency (str):
        locale (str):
        date_format (str):
        month_start_day (int):
        moniker (FamilySettingsMoniker):
        default_account_sharing (FamilySettingsDefaultAccountSharing):
        custom_enabled_currencies (bool):
        enabled_currencies (list[str]):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (None | str | Unset):
        country (None | str | Unset):
        timezone (None | str | Unset):
    """

    id: UUID
    currency: str
    locale: str
    date_format: str
    month_start_day: int
    moniker: FamilySettingsMoniker
    default_account_sharing: FamilySettingsDefaultAccountSharing
    custom_enabled_currencies: bool
    enabled_currencies: list[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    timezone: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        currency = self.currency

        locale = self.locale

        date_format = self.date_format

        month_start_day = self.month_start_day

        moniker = self.moniker.value

        default_account_sharing = self.default_account_sharing.value

        custom_enabled_currencies = self.custom_enabled_currencies

        enabled_currencies = self.enabled_currencies

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        timezone: None | str | Unset
        if isinstance(self.timezone, Unset):
            timezone = UNSET
        else:
            timezone = self.timezone

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "currency": currency,
                "locale": locale,
                "date_format": date_format,
                "month_start_day": month_start_day,
                "moniker": moniker,
                "default_account_sharing": default_account_sharing,
                "custom_enabled_currencies": custom_enabled_currencies,
                "enabled_currencies": enabled_currencies,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if country is not UNSET:
            field_dict["country"] = country
        if timezone is not UNSET:
            field_dict["timezone"] = timezone

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        currency = d.pop("currency")

        locale = d.pop("locale")

        date_format = d.pop("date_format")

        month_start_day = d.pop("month_start_day")

        moniker = FamilySettingsMoniker(d.pop("moniker"))

        default_account_sharing = FamilySettingsDefaultAccountSharing(d.pop("default_account_sharing"))

        custom_enabled_currencies = d.pop("custom_enabled_currencies")

        enabled_currencies = cast(list[str], d.pop("enabled_currencies"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        def _parse_timezone(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        timezone = _parse_timezone(d.pop("timezone", UNSET))

        family_settings = cls(
            id=id,
            currency=currency,
            locale=locale,
            date_format=date_format,
            month_start_day=month_start_day,
            moniker=moniker,
            default_account_sharing=default_account_sharing,
            custom_enabled_currencies=custom_enabled_currencies,
            enabled_currencies=enabled_currencies,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            country=country,
            timezone=timezone,
        )

        family_settings.additional_properties = d
        return family_settings

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
