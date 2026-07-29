from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostApiV1ValuationsBodyValuation")


@_attrs_define
class PostApiV1ValuationsBodyValuation:
    """
    Attributes:
        account_id (UUID): Account ID (required)
        amount (float): Valuation amount (required)
        date (datetime.date): Valuation date (required)
        notes (str | Unset): Additional notes
        upsert (bool | Unset): Nested alternative to the top-level response-status flag. Top-level upsert takes
            precedence when both are provided.
    """

    account_id: UUID
    amount: float
    date: datetime.date
    notes: str | Unset = UNSET
    upsert: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = str(self.account_id)

        amount = self.amount

        date = self.date.isoformat()

        notes = self.notes

        upsert = self.upsert

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "account_id": account_id,
                "amount": amount,
                "date": date,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes
        if upsert is not UNSET:
            field_dict["upsert"] = upsert

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = UUID(d.pop("account_id"))

        amount = d.pop("amount")

        date = datetime.date.fromisoformat(d.pop("date"))

        notes = d.pop("notes", UNSET)

        upsert = d.pop("upsert", UNSET)

        post_api_v1_valuations_body_valuation = cls(
            account_id=account_id,
            amount=amount,
            date=date,
            notes=notes,
            upsert=upsert,
        )

        post_api_v1_valuations_body_valuation.additional_properties = d
        return post_api_v1_valuations_body_valuation

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
