from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PatchApiV1ValuationsIdBodyValuation")


@_attrs_define
class PatchApiV1ValuationsIdBodyValuation:
    """
    Attributes:
        amount (float | Unset): New valuation amount (must provide with date)
        date (datetime.date | Unset): New valuation date (must provide with amount)
        notes (str | Unset): Additional notes
    """

    amount: float | Unset = UNSET
    date: datetime.date | Unset = UNSET
    notes: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        amount = self.amount

        date: str | Unset = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if amount is not UNSET:
            field_dict["amount"] = amount
        if date is not UNSET:
            field_dict["date"] = date
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        amount = d.pop("amount", UNSET)

        _date = d.pop("date", UNSET)
        date: datetime.date | Unset
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = datetime.date.fromisoformat(_date)

        notes = d.pop("notes", UNSET)

        patch_api_v1_valuations_id_body_valuation = cls(
            amount=amount,
            date=date,
            notes=notes,
        )

        patch_api_v1_valuations_id_body_valuation.additional_properties = d
        return patch_api_v1_valuations_id_body_valuation

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
