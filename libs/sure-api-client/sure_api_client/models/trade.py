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
    from ..models.trade_category_type_0 import TradeCategoryType0
    from ..models.trade_security_type_0 import TradeSecurityType0


T = TypeVar("T", bound="Trade")


@_attrs_define
class Trade:
    """
    Attributes:
        id (UUID):
        date (datetime.date):
        amount (str):
        currency (str):
        name (str):
        qty (str):
        price (str):
        account (Account):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        notes (None | str | Unset):
        investment_activity_label (None | str | Unset):
        security (None | TradeSecurityType0 | Unset):
        category (None | TradeCategoryType0 | Unset):
    """

    id: UUID
    date: datetime.date
    amount: str
    currency: str
    name: str
    qty: str
    price: str
    account: Account
    created_at: datetime.datetime
    updated_at: datetime.datetime
    notes: None | str | Unset = UNSET
    investment_activity_label: None | str | Unset = UNSET
    security: None | TradeSecurityType0 | Unset = UNSET
    category: None | TradeCategoryType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.trade_category_type_0 import TradeCategoryType0
        from ..models.trade_security_type_0 import TradeSecurityType0

        id = str(self.id)

        date = self.date.isoformat()

        amount = self.amount

        currency = self.currency

        name = self.name

        qty = self.qty

        price = self.price

        account = self.account.to_dict()

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        notes: None | str | Unset
        if isinstance(self.notes, Unset):
            notes = UNSET
        else:
            notes = self.notes

        investment_activity_label: None | str | Unset
        if isinstance(self.investment_activity_label, Unset):
            investment_activity_label = UNSET
        else:
            investment_activity_label = self.investment_activity_label

        security: dict[str, Any] | None | Unset
        if isinstance(self.security, Unset):
            security = UNSET
        elif isinstance(self.security, TradeSecurityType0):
            security = self.security.to_dict()
        else:
            security = self.security

        category: dict[str, Any] | None | Unset
        if isinstance(self.category, Unset):
            category = UNSET
        elif isinstance(self.category, TradeCategoryType0):
            category = self.category.to_dict()
        else:
            category = self.category

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "date": date,
                "amount": amount,
                "currency": currency,
                "name": name,
                "qty": qty,
                "price": price,
                "account": account,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if notes is not UNSET:
            field_dict["notes"] = notes
        if investment_activity_label is not UNSET:
            field_dict["investment_activity_label"] = investment_activity_label
        if security is not UNSET:
            field_dict["security"] = security
        if category is not UNSET:
            field_dict["category"] = category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.account import Account
        from ..models.trade_category_type_0 import TradeCategoryType0
        from ..models.trade_security_type_0 import TradeSecurityType0

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        date = datetime.date.fromisoformat(d.pop("date"))

        amount = d.pop("amount")

        currency = d.pop("currency")

        name = d.pop("name")

        qty = d.pop("qty")

        price = d.pop("price")

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

        def _parse_investment_activity_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        investment_activity_label = _parse_investment_activity_label(d.pop("investment_activity_label", UNSET))

        def _parse_security(data: object) -> None | TradeSecurityType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                security_type_0 = TradeSecurityType0.from_dict(data)

                return security_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TradeSecurityType0 | Unset, data)

        security = _parse_security(d.pop("security", UNSET))

        def _parse_category(data: object) -> None | TradeCategoryType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                category_type_0 = TradeCategoryType0.from_dict(data)

                return category_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TradeCategoryType0 | Unset, data)

        category = _parse_category(d.pop("category", UNSET))

        trade = cls(
            id=id,
            date=date,
            amount=amount,
            currency=currency,
            name=name,
            qty=qty,
            price=price,
            account=account,
            created_at=created_at,
            updated_at=updated_at,
            notes=notes,
            investment_activity_label=investment_activity_label,
            security=security,
            category=category,
        )

        trade.additional_properties = d
        return trade

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
