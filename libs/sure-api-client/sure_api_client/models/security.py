from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.security_kind import SecurityKind
from ..types import UNSET, Unset

T = TypeVar("T", bound="Security")


@_attrs_define
class Security:
    """
    Attributes:
        id (UUID):
        ticker (str):
        kind (SecurityKind):
        offline (bool):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        name (None | str | Unset):
        country_code (None | str | Unset):
        exchange_mic (None | str | Unset):
        exchange_acronym (None | str | Unset):
        exchange_operating_mic (None | str | Unset):
        exchange_name (None | str | Unset):
        offline_reason (None | str | Unset):
        website_url (None | str | Unset):
        logo_url (None | str | Unset):
        first_provider_price_on (datetime.date | None | Unset):
    """

    id: UUID
    ticker: str
    kind: SecurityKind
    offline: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    name: None | str | Unset = UNSET
    country_code: None | str | Unset = UNSET
    exchange_mic: None | str | Unset = UNSET
    exchange_acronym: None | str | Unset = UNSET
    exchange_operating_mic: None | str | Unset = UNSET
    exchange_name: None | str | Unset = UNSET
    offline_reason: None | str | Unset = UNSET
    website_url: None | str | Unset = UNSET
    logo_url: None | str | Unset = UNSET
    first_provider_price_on: datetime.date | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        ticker = self.ticker

        kind = self.kind.value

        offline = self.offline

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        country_code: None | str | Unset
        if isinstance(self.country_code, Unset):
            country_code = UNSET
        else:
            country_code = self.country_code

        exchange_mic: None | str | Unset
        if isinstance(self.exchange_mic, Unset):
            exchange_mic = UNSET
        else:
            exchange_mic = self.exchange_mic

        exchange_acronym: None | str | Unset
        if isinstance(self.exchange_acronym, Unset):
            exchange_acronym = UNSET
        else:
            exchange_acronym = self.exchange_acronym

        exchange_operating_mic: None | str | Unset
        if isinstance(self.exchange_operating_mic, Unset):
            exchange_operating_mic = UNSET
        else:
            exchange_operating_mic = self.exchange_operating_mic

        exchange_name: None | str | Unset
        if isinstance(self.exchange_name, Unset):
            exchange_name = UNSET
        else:
            exchange_name = self.exchange_name

        offline_reason: None | str | Unset
        if isinstance(self.offline_reason, Unset):
            offline_reason = UNSET
        else:
            offline_reason = self.offline_reason

        website_url: None | str | Unset
        if isinstance(self.website_url, Unset):
            website_url = UNSET
        else:
            website_url = self.website_url

        logo_url: None | str | Unset
        if isinstance(self.logo_url, Unset):
            logo_url = UNSET
        else:
            logo_url = self.logo_url

        first_provider_price_on: None | str | Unset
        if isinstance(self.first_provider_price_on, Unset):
            first_provider_price_on = UNSET
        elif isinstance(self.first_provider_price_on, datetime.date):
            first_provider_price_on = self.first_provider_price_on.isoformat()
        else:
            first_provider_price_on = self.first_provider_price_on

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ticker": ticker,
                "kind": kind,
                "offline": offline,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if country_code is not UNSET:
            field_dict["country_code"] = country_code
        if exchange_mic is not UNSET:
            field_dict["exchange_mic"] = exchange_mic
        if exchange_acronym is not UNSET:
            field_dict["exchange_acronym"] = exchange_acronym
        if exchange_operating_mic is not UNSET:
            field_dict["exchange_operating_mic"] = exchange_operating_mic
        if exchange_name is not UNSET:
            field_dict["exchange_name"] = exchange_name
        if offline_reason is not UNSET:
            field_dict["offline_reason"] = offline_reason
        if website_url is not UNSET:
            field_dict["website_url"] = website_url
        if logo_url is not UNSET:
            field_dict["logo_url"] = logo_url
        if first_provider_price_on is not UNSET:
            field_dict["first_provider_price_on"] = first_provider_price_on

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        ticker = d.pop("ticker")

        kind = SecurityKind(d.pop("kind"))

        offline = d.pop("offline")

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_country_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country_code = _parse_country_code(d.pop("country_code", UNSET))

        def _parse_exchange_mic(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exchange_mic = _parse_exchange_mic(d.pop("exchange_mic", UNSET))

        def _parse_exchange_acronym(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exchange_acronym = _parse_exchange_acronym(d.pop("exchange_acronym", UNSET))

        def _parse_exchange_operating_mic(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exchange_operating_mic = _parse_exchange_operating_mic(d.pop("exchange_operating_mic", UNSET))

        def _parse_exchange_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exchange_name = _parse_exchange_name(d.pop("exchange_name", UNSET))

        def _parse_offline_reason(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        offline_reason = _parse_offline_reason(d.pop("offline_reason", UNSET))

        def _parse_website_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        website_url = _parse_website_url(d.pop("website_url", UNSET))

        def _parse_logo_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        logo_url = _parse_logo_url(d.pop("logo_url", UNSET))

        def _parse_first_provider_price_on(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                first_provider_price_on_type_0 = datetime.date.fromisoformat(data)

                return first_provider_price_on_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        first_provider_price_on = _parse_first_provider_price_on(d.pop("first_provider_price_on", UNSET))

        security = cls(
            id=id,
            ticker=ticker,
            kind=kind,
            offline=offline,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            country_code=country_code,
            exchange_mic=exchange_mic,
            exchange_acronym=exchange_acronym,
            exchange_operating_mic=exchange_operating_mic,
            exchange_name=exchange_name,
            offline_reason=offline_reason,
            website_url=website_url,
            logo_url=logo_url,
            first_provider_price_on=first_provider_price_on,
        )

        security.additional_properties = d
        return security

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
