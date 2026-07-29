from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SecurityPriceSecurity")


@_attrs_define
class SecurityPriceSecurity:
    """
    Attributes:
        id (UUID):
        ticker (str):
        name (None | str | Unset):
        exchange_operating_mic (None | str | Unset):
    """

    id: UUID
    ticker: str
    name: None | str | Unset = UNSET
    exchange_operating_mic: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        ticker = self.ticker

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        exchange_operating_mic: None | str | Unset
        if isinstance(self.exchange_operating_mic, Unset):
            exchange_operating_mic = UNSET
        else:
            exchange_operating_mic = self.exchange_operating_mic

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "ticker": ticker,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if exchange_operating_mic is not UNSET:
            field_dict["exchange_operating_mic"] = exchange_operating_mic

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = UUID(d.pop("id"))

        ticker = d.pop("ticker")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_exchange_operating_mic(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exchange_operating_mic = _parse_exchange_operating_mic(d.pop("exchange_operating_mic", UNSET))

        security_price_security = cls(
            id=id,
            ticker=ticker,
            name=name,
            exchange_operating_mic=exchange_operating_mic,
        )

        security_price_security.additional_properties = d
        return security_price_security

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
