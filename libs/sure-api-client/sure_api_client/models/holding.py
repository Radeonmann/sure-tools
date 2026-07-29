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
    from ..models.holding_security import HoldingSecurity


T = TypeVar("T", bound="Holding")


@_attrs_define
class Holding:
    """
    Attributes:
        id (UUID):
        date (datetime.date):
        qty (str): Quantity of shares held
        price (str): Formatted price per share
        amount (str):
        currency (str):
        account (Account):
        security (HoldingSecurity):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        cost_basis_source (None | str | Unset):
        avg_cost (None | str | Unset):
    """

    id: UUID
    date: datetime.date
    qty: str
    price: str
    amount: str
    currency: str
    account: Account
    security: HoldingSecurity
    created_at: datetime.datetime
    updated_at: datetime.datetime
    cost_basis_source: None | str | Unset = UNSET
    avg_cost: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        date = self.date.isoformat()

        qty = self.qty

        price = self.price

        amount = self.amount

        currency = self.currency

        account = self.account.to_dict()

        security = self.security.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        cost_basis_source: None | str | Unset
        if isinstance(self.cost_basis_source, Unset):
            cost_basis_source = UNSET
        else:
            cost_basis_source = self.cost_basis_source

        avg_cost: None | str | Unset
        if isinstance(self.avg_cost, Unset):
            avg_cost = UNSET
        else:
            avg_cost = self.avg_cost

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "qty": qty,
                "price": price,
                "amount": amount,
                "currency": currency,
                "account": account,
                "security": security,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if cost_basis_source is not UNSET:
            field_dict["cost_basis_source"] = cost_basis_source
        if avg_cost is not UNSET:
            field_dict["avg_cost"] = avg_cost

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.holding_security import HoldingSecurity

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        date = datetime.date.fromisoformat(d.pop("date"))

        qty = d.pop("qty")

        price = d.pop("price")

        amount = d.pop("amount")

        currency = d.pop("currency")

        account = Account.from_dict(d.pop("account"))

        security = HoldingSecurity.from_dict(d.pop("security"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        def _parse_cost_basis_source(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        cost_basis_source = _parse_cost_basis_source(d.pop("cost_basis_source", UNSET))

        def _parse_avg_cost(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        avg_cost = _parse_avg_cost(d.pop("avg_cost", UNSET))

        holding = cls(
            id=id,
            date=date,
            qty=qty,
            price=price,
            amount=amount,
            currency=currency,
            account=account,
            security=security,
            created_at=created_at,
            updated_at=updated_at,
            cost_basis_source=cost_basis_source,
            avg_cost=avg_cost,
        )

        holding.additional_properties = d
        return holding

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
