from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account


T = TypeVar("T", bound="Valuation")


@_attrs_define
class Valuation:
    """
    Attributes:
        id (UUID):
        date (datetime.date):
        amount (str):
        currency (str):
        kind (str):
        account (Account):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        notes (None | str | Unset):
    """

    id: UUID
    date: datetime.date
    amount: str
    currency: str
    kind: str
    account: Account
    created_at: datetime.datetime
    updated_at: datetime.datetime
    notes: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        date = self.date.isoformat()

        amount = self.amount

        currency = self.currency

        kind = self.kind

        account = self.account.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "amount": amount,
                "currency": currency,
                "kind": kind,
                "account": account,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        date = datetime.date.fromisoformat(d.pop("date"))

        amount = d.pop("amount")

        currency = d.pop("currency")

        kind = d.pop("kind")

        account = Account.from_dict(d.pop("account"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_notes(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        notes = _parse_notes(d.pop("notes", UNSET))

        valuation = cls(
            id=id,
            date=date,
            amount=amount,
            currency=currency,
            kind=kind,
            account=account,
            created_at=created_at,
            updated_at=updated_at,
            notes=notes,
        )

        valuation.additional_properties = d
        return valuation

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
