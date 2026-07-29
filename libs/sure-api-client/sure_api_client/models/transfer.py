from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.account import Account


T = TypeVar("T", bound="Transfer")


@_attrs_define
class Transfer:
    """
    Attributes:
        id (UUID):
        amount (str):
        currency (str):
        other_account (Account | Unset):
    """

    id: UUID
    amount: str
    currency: str
    other_account: Account | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        amount = self.amount

        currency = self.currency

        other_account: dict[str, Any] | Unset = UNSET
        if not isinstance(self.other_account, Unset):
            other_account = self.other_account.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "amount": amount,
                "currency": currency,
            }
        )
        if other_account is not UNSET:
            field_dict["other_account"] = other_account

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        amount = d.pop("amount")

        currency = d.pop("currency")

        _other_account = d.pop("other_account", UNSET)
        other_account: Account | Unset
        if isinstance(_other_account, Unset):
            other_account = UNSET
        else:
            other_account = Account.from_dict(_other_account)

        transfer = cls(
            id=id,
            amount=amount,
            currency=currency,
            other_account=other_account,
        )

        transfer.additional_properties = d
        return transfer

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
