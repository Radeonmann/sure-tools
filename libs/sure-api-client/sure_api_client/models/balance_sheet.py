from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.money import Money


T = TypeVar("T", bound="BalanceSheet")


@_attrs_define
class BalanceSheet:
    """
    Attributes:
        currency (str): Family primary currency
        net_worth (Money):
        assets (Money):
        liabilities (Money):
    """

    currency: str
    net_worth: Money
    assets: Money
    liabilities: Money
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        currency = self.currency

        net_worth = self.net_worth.to_dict()

        assets = self.assets.to_dict()

        liabilities = self.liabilities.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "currency": currency,
                "net_worth": net_worth,
                "assets": assets,
                "liabilities": liabilities,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.money import Money

        d = dict(src_dict)
        currency = d.pop("currency")

        net_worth = Money.from_dict(d.pop("net_worth"))

        assets = Money.from_dict(d.pop("assets"))

        liabilities = Money.from_dict(d.pop("liabilities"))

        balance_sheet = cls(
            currency=currency,
            net_worth=net_worth,
            assets=assets,
            liabilities=liabilities,
        )

        balance_sheet.additional_properties = d
        return balance_sheet

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
