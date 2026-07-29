from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.transaction_response_account import TransactionResponseAccount


T = TypeVar("T", bound="TransactionResponse")


@_attrs_define
class TransactionResponse:
    """
    Attributes:
        id (UUID):
        date (datetime.date):
        amount (str):
        currency (str):
        name (str):
        entryable_type (str):
        account (TransactionResponseAccount):
    """

    id: UUID
    date: datetime.date
    amount: str
    currency: str
    name: str
    entryable_type: str
    account: TransactionResponseAccount
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        date = self.date.isoformat()

        amount = self.amount

        currency = self.currency

        name = self.name

        entryable_type = self.entryable_type

        account = self.account.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "amount": amount,
                "currency": currency,
                "name": name,
                "entryable_type": entryable_type,
                "account": account,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.transaction_response_account import TransactionResponseAccount

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        date = datetime.date.fromisoformat(d.pop("date"))

        amount = d.pop("amount")

        currency = d.pop("currency")

        name = d.pop("name")

        entryable_type = d.pop("entryable_type")

        account = TransactionResponseAccount.from_dict(d.pop("account"))

        transaction_response = cls(
            id=id,
            date=date,
            amount=amount,
            currency=currency,
            name=name,
            entryable_type=entryable_type,
            account=account,
        )

        transaction_response.additional_properties = d
        return transaction_response

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
