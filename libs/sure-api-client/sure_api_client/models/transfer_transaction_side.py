from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.transfer_transaction_side_account import TransferTransactionSideAccount


T = TypeVar("T", bound="TransferTransactionSide")


@_attrs_define
class TransferTransactionSide:
    """
    Attributes:
        id (UUID):
        entry_id (UUID):
        date (datetime.date):
        amount (str):
        amount_cents (int): Signed amount in currency minor units
        currency (str):
        name (str):
        kind (str):
        account (TransferTransactionSideAccount):
    """

    id: UUID
    entry_id: UUID
    date: datetime.date
    amount: str
    amount_cents: int
    currency: str
    name: str
    kind: str
    account: TransferTransactionSideAccount
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        entry_id = str(self.entry_id)

        date = self.date.isoformat()

        amount = self.amount

        amount_cents = self.amount_cents

        currency = self.currency

        name = self.name

        kind = self.kind

        account = self.account.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "entry_id": entry_id,
                "date": date,
                "amount": amount,
                "amount_cents": amount_cents,
                "currency": currency,
                "name": name,
                "kind": kind,
                "account": account,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transfer_transaction_side_account import TransferTransactionSideAccount

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        entry_id = UUID(d.pop("entry_id"))

        date = datetime.date.fromisoformat(d.pop("date"))

        amount = d.pop("amount")

        amount_cents = d.pop("amount_cents")

        currency = d.pop("currency")

        name = d.pop("name")

        kind = d.pop("kind")

        account = TransferTransactionSideAccount.from_dict(d.pop("account"))

        transfer_transaction_side = cls(
            id=id,
            entry_id=entry_id,
            date=date,
            amount=amount,
            amount_cents=amount_cents,
            currency=currency,
            name=name,
            kind=kind,
            account=account,
        )

        transfer_transaction_side.additional_properties = d
        return transfer_transaction_side

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
