from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.patch_api_v1_trades_id_body_trade_nature import PatchApiV1TradesIdBodyTradeNature
from ..models.patch_api_v1_trades_id_body_trade_type import PatchApiV1TradesIdBodyTradeType
from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiV1TradesIdBodyTrade")


@_attrs_define
class PatchApiV1TradesIdBodyTrade:
    """
    Attributes:
        date (datetime.date | Unset):
        qty (float | Unset):
        price (float | Unset):
        type_ (PatchApiV1TradesIdBodyTradeType | Unset):
        nature (PatchApiV1TradesIdBodyTradeNature | Unset):
        name (str | Unset):
        notes (str | Unset):
        currency (str | Unset):
        investment_activity_label (str | Unset):
        category_id (UUID | Unset):
    """

    date: datetime.date | Unset = UNSET
    qty: float | Unset = UNSET
    price: float | Unset = UNSET
    type_: PatchApiV1TradesIdBodyTradeType | Unset = UNSET
    nature: PatchApiV1TradesIdBodyTradeNature | Unset = UNSET
    name: str | Unset = UNSET
    notes: str | Unset = UNSET
    currency: str | Unset = UNSET
    investment_activity_label: str | Unset = UNSET
    category_id: UUID | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        qty = self.qty

        price = self.price

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        nature: str | Unset = UNSET
        if not isinstance(self.nature, Unset):
            nature = self.nature.value

        name = self.name

        notes = self.notes

        currency = self.currency

        investment_activity_label = self.investment_activity_label

        category_id: str | Unset = UNSET
        if not isinstance(self.category_id, Unset):
            category_id = str(self.category_id)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date is not UNSET:
            field_dict["date"] = date
        if qty is not UNSET:
            field_dict["qty"] = qty
        if price is not UNSET:
            field_dict["price"] = price
        if type_ is not UNSET:
            field_dict["type"] = type_
        if nature is not UNSET:
            field_dict["nature"] = nature
        if name is not UNSET:
            field_dict["name"] = name
        if notes is not UNSET:
            field_dict["notes"] = notes
        if currency is not UNSET:
            field_dict["currency"] = currency
        if investment_activity_label is not UNSET:
            field_dict["investment_activity_label"] = investment_activity_label
        if category_id is not UNSET:
            field_dict["category_id"] = category_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = datetime.date.fromisoformat(_date)

        qty = d.pop("qty", UNSET)

        price = d.pop("price", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: PatchApiV1TradesIdBodyTradeType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = PatchApiV1TradesIdBodyTradeType(_type_)

        _nature = d.pop("nature", UNSET)
        nature: PatchApiV1TradesIdBodyTradeNature | Unset
        if isinstance(_nature, Unset):
            nature = UNSET
        else:
            nature = PatchApiV1TradesIdBodyTradeNature(_nature)

        name = d.pop("name", UNSET)

        notes = d.pop("notes", UNSET)

        currency = d.pop("currency", UNSET)

        investment_activity_label = d.pop("investment_activity_label", UNSET)

        _category_id = d.pop("category_id", UNSET)
        category_id: UUID | Unset
        if isinstance(_category_id, Unset):
            category_id = UNSET
        else:
            category_id = UUID(_category_id)

        patch_api_v1_trades_id_body_trade = cls(
            date=date,
            qty=qty,
            price=price,
            type_=type_,
            nature=nature,
            name=name,
            notes=notes,
            currency=currency,
            investment_activity_label=investment_activity_label,
            category_id=category_id,
        )

        patch_api_v1_trades_id_body_trade.additional_properties = d
        return patch_api_v1_trades_id_body_trade

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
