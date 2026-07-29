from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.security_price_security import SecurityPriceSecurity


T = TypeVar("T", bound="SecurityPrice")


@_attrs_define
class SecurityPrice:
    """
    Attributes:
        id (UUID):
        date (datetime.date):
        price (str): Formatted security price
        price_amount (str): Exact decimal security price
        currency (str):
        provisional (bool):
        security (SecurityPriceSecurity):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
    """

    id: UUID
    date: datetime.date
    price: str
    price_amount: str
    currency: str
    provisional: bool
    security: SecurityPriceSecurity
    created_at: datetime.datetime
    updated_at: datetime.datetime
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        date = self.date.isoformat()

        price = self.price

        price_amount = self.price_amount

        currency = self.currency

        provisional = self.provisional

        security = self.security.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "price": price,
                "price_amount": price_amount,
                "currency": currency,
                "provisional": provisional,
                "security": security,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.security_price_security import SecurityPriceSecurity

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        date = datetime.date.fromisoformat(d.pop("date"))

        price = d.pop("price")

        price_amount = d.pop("price_amount")

        currency = d.pop("currency")

        provisional = d.pop("provisional")

        security = SecurityPriceSecurity.from_dict(d.pop("security"))

        created_at = datetime.datetime.fromisoformat(d.pop("created_at"))

        updated_at = datetime.datetime.fromisoformat(d.pop("updated_at"))

        security_price = cls(
            id=id,
            date=date,
            price=price,
            price_amount=price_amount,
            currency=currency,
            provisional=provisional,
            security=security,
            created_at=created_at,
            updated_at=updated_at,
        )

        security_price.additional_properties = d
        return security_price

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
